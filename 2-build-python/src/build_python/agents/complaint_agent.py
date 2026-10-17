"""Agent 2: registers a user complaint."""

from build_python.tools.ticket_store import create_ticket


def run(detail: str) -> str:
    ticket_id = create_ticket("complaint", detail)
    return f"Complaint registered. Your ticket id is {ticket_id}."
