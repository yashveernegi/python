"""A tiny in-memory knowledge base the agents look things up in."""

PLANS = {
    "default": "Plan: Smart-199 | 2GB/day | unlimited calls | 100 SMS/day",
}

SERVICES = [
    "5G upgrade",
    "International roaming pack",
    "OTT bundle (streaming apps)",
    "Weekend data booster",
]


def lookup_plan(customer_id: str) -> str:
    return PLANS.get(customer_id, PLANS["default"])


def available_services() -> list[str]:
    return SERVICES
