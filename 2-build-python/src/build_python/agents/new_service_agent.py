"""Agent 4: lists newly available services."""

from build_python.tools.knowledge_base import available_services


def run() -> str:
    services = ", ".join(available_services())
    return f"New services available: {services}"
