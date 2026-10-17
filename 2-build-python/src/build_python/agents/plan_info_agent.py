"""Agent 3: gives current plan information."""

from build_python.tools.knowledge_base import lookup_plan


def run(customer_id: str = "default") -> str:
    return f"Your current plan: {lookup_plan(customer_id)}"
