"""A tiny in-memory store for complaints and billing records."""

_tickets: list[dict[str, str]] = []


def create_ticket(category: str, detail: str) -> str:
    ticket_id = f"TKT-{len(_tickets) + 1:04d}"
    _tickets.append({"id": ticket_id, "category": category, "detail": detail})
    return ticket_id


def get_balance(customer_id: str) -> str:
    # Fixed demo value; a real system would query a billing service.
    return f"Customer {customer_id}: outstanding balance 249.00, due in 7 days"
