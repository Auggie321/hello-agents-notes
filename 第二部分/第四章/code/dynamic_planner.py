"""Minimal dynamic replanning and hierarchical planning example."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class StepStatus(str, Enum):
    PENDING = "pending"
    DONE = "done"
    FAILED = "failed"


@dataclass
class PlanStep:
    goal: str
    status: StepStatus = StepStatus.PENDING
    result: str | None = None
    error: str | None = None
    sub_steps: list["PlanStep"] = field(default_factory=list)


@dataclass
class Plan:
    task: str
    steps: list[PlanStep]
    replan_count: int = 0


class DynamicPlanner:
    def __init__(self, max_replans: int = 2):
        self.max_replans = max_replans

    def make_travel_plan(self, task: str) -> Plan:
        return Plan(
            task=task,
            steps=[
                PlanStep("确认时间、预算、出行偏好"),
                PlanStep(
                    "预订交通",
                    sub_steps=[
                        PlanStep("查询航班或高铁"),
                        PlanStep("筛选合适班次"),
                        PlanStep("下单并保存凭证"),
                    ],
                ),
                PlanStep("预订酒店"),
                PlanStep("安排本地交通"),
                PlanStep("汇总行程并请用户确认"),
            ],
        )

    def replan_after_failure(self, plan: Plan, failed_index: int, error: str) -> Plan:
        if plan.replan_count >= self.max_replans:
            raise RuntimeError("Replanning limit reached; hand off to a human operator.")

        failed_step = plan.steps[failed_index]
        failed_step.status = StepStatus.FAILED
        failed_step.error = error
        plan.replan_count += 1

        replacement = self._make_replacement_step(failed_step, error)
        plan.steps[failed_index] = replacement
        return plan

    def _make_replacement_step(self, failed_step: PlanStep, error: str) -> PlanStep:
        if "sold out" in error.lower() or "售罄" in error:
            return PlanStep(
                goal=f"为失败步骤寻找替代方案：{failed_step.goal}",
                sub_steps=[
                    PlanStep("放宽时间或价格条件重新查询"),
                    PlanStep("提供 2 到 3 个替代选项"),
                    PlanStep("向用户确认后继续执行"),
                ],
            )

        return PlanStep(
            goal=f"重新执行并修正参数：{failed_step.goal}",
            sub_steps=[
                PlanStep("分析失败原因"),
                PlanStep("修正工具参数或业务约束"),
                PlanStep("重试该步骤"),
            ],
        )


if __name__ == "__main__":
    planner = DynamicPlanner()
    plan = planner.make_travel_plan("预订一次从北京到上海的商务旅行")
    plan = planner.replan_after_failure(plan, failed_index=1, error="航班售罄")
    for index, step in enumerate(plan.steps, start=1):
        print(index, step.goal, step.status)
