"""Agent 1: takes the caller's response and decides which specialist to route to."""

KEYWORDS = {
    "complaint": "complaint",
    "complain": "complaint",
    "issue": "complaint",
    "plan": "plan_info",
    "balance plan": "plan_info",
    "service": "new_service",
    "offer": "new_service",
    "upgrade": "new_service",
    "network": "technical",
    "slow": "technical",
    "signal": "technical",
    "no internet": "technical",
    "bill": "billing",
    "payment": "billing",
    "charge": "billing",
    "recharge": "billing",
}


def classify(user_response: str) -> str:
    """Return the intent/category for a caller's free-text response."""
    text = user_response.lower()
    for keyword, intent in KEYWORDS.items():
        if keyword in text:
            return intent
    return "complaint"  # safe default: log it as a complaint for a human
