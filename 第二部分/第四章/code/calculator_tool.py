"""Calculator tool and failure handling for a ReAct-style tool executor."""

from __future__ import annotations

import ast
import operator
from dataclasses import dataclass, field


class ToolError(ValueError):
    """Raised when a tool cannot process the provided input."""


class SafeCalculator:
    """Evaluate arithmetic expressions with a small safe AST interpreter."""

    _binary_ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
    }
    _unary_ops = {
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    def run(self, expression: str) -> float | int:
        try:
            tree = ast.parse(expression, mode="eval")
        except SyntaxError as exc:
            raise ToolError("Expression is not valid arithmetic syntax.") from exc
        return self._eval(tree.body)

    def _eval(self, node: ast.AST) -> float | int:
        if isinstance(node, ast.Constant) and isinstance(node.value, int | float):
            return node.value

        if isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type not in self._binary_ops:
                raise ToolError(f"Operator {op_type.__name__} is not allowed.")
            return self._binary_ops[op_type](self._eval(node.left), self._eval(node.right))

        if isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type not in self._unary_ops:
                raise ToolError(f"Operator {op_type.__name__} is not allowed.")
            return self._unary_ops[op_type](self._eval(node.operand))

        raise ToolError(f"Unsupported expression node: {type(node).__name__}.")


@dataclass
class ToolExecutor:
    max_failures: int = 2
    failure_count: int = 0
    tools: dict[str, object] = field(default_factory=lambda: {"calculator": SafeCalculator()})

    def execute(self, tool_name: str, tool_input: str) -> str:
        tool = self.tools.get(tool_name)
        if tool is None:
            return self._handle_failure(
                f"Unknown tool '{tool_name}'. Choose one of: {list(self.tools)}."
            )

        try:
            result = tool.run(tool_input)
        except ToolError as exc:
            return self._handle_failure(str(exc))

        self.failure_count = 0
        return f"Observation: {result}"

    def _handle_failure(self, reason: str) -> str:
        self.failure_count += 1
        if self.failure_count >= self.max_failures:
            return (
                "Observation: tool call failed repeatedly. Re-check the task, "
                "select the most suitable tool, and pass only the required argument. "
                f"Last error: {reason}"
            )
        return f"Observation: tool call failed. Please correct the tool call. Error: {reason}"


if __name__ == "__main__":
    executor = ToolExecutor()
    print(executor.execute("calculator", "(123 + 456) * 789 / 12"))
