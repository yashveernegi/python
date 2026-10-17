"""Agent 5: technical problem resolution."""

from build_python.tools.ticket_store import create_ticket


def run(detail: str) -> str:
    # First try a self-serve fix; escalate to a ticket if it looks unresolved.
    if "slow" in detail.lower() or "no internet" in detail.lower():
        return (
            "Please toggle airplane mode for 10 seconds, then retry. "
            "This fixes most speed issues."
        )
    ticket_id = create_ticket("technical", detail)
    return f"Technical issue logged for an engineer. Ticket id {ticket_id}."
