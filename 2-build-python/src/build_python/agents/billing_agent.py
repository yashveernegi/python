"""Agent 6: billing and payments."""

from build_python.tools.ticket_store import get_balance


def run(customer_id: str = "default") -> str:
    return get_balance(customer_id)
