"""Structured output parsing for a ReAct-style agent.

This example replaces fragile regex parsing with JSON parsing plus
lightweight validation. It uses only Python standard library modules.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from typing import Any


@dataclass(frozen=True)
class ToolCall:
    name: str
    input: str


@dataclass(frozen=True)
class AgentStep:
    thought: str
    action: ToolCall | None = None
    final_answer: str | None = None


class ParseError(ValueError):
    """Raised when a model response is not a valid agent step."""


def parse_agent_step(raw_text: str) -> AgentStep:
    """Parse a JSON model response into an AgentStep."""

    try:
        payload: dict[str, Any] = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        raise ParseError(f"Model output is not valid JSON: {exc}") from exc

    thought = payload.get("thought")
    if not isinstance(thought, str) or not thought.strip():
        raise ParseError("Field 'thought' must be a non-empty string.")

    action_payload = payload.get("action")
    final_answer = payload.get("final_answer")

    if action_payload is None and final_answer is None:
        raise ParseError("Either 'action' or 'final_answer' must be provided.")

    if action_payload is not None and final_answer is not None:
        raise ParseError("Only one of 'action' and 'final_answer' can be provided.")

    action = None
    if action_payload is not None:
        if not isinstance(action_payload, dict):
            raise ParseError("Field 'action' must be an object.")

        name = action_payload.get("name")
        tool_input = action_payload.get("input")
        if not isinstance(name, str) or not name.strip():
            raise ParseError("Field 'action.name' must be a non-empty string.")
        if not isinstance(tool_input, str):
            raise ParseError("Field 'action.input' must be a string.")

        action = ToolCall(name=name.strip(), input=tool_input)

    if final_answer is not None and not isinstance(final_answer, str):
        raise ParseError("Field 'final_answer' must be a string when provided.")

    return AgentStep(
        thought=thought.strip(),
        action=action,
        final_answer=final_answer,
    )


if __name__ == "__main__":
    raw = """
    {
      "thought": "这是确定性数学计算，应该调用计算器。",
      "action": {"name": "calculator", "input": "(123 + 456) * 789 / 12"},
      "final_answer": null
    }
    """
    print(parse_agent_step(raw))
