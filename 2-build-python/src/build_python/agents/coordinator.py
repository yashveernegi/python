"""The coordinator wires the agents together.

Flow:
  caller text -> Agent   (reception) classifies intent
             -> coordinator dispatches to the matching specialist agent
             -> specialist agent uses tools and returns a reply
"""

from build_python.agents import (
    billing_agent,
    complaint_agent,
    new_service_agent,
    plan_info_agent,
    reception_agent,
    technical_agent,
)


def run(user_response: str) -> str:
    # Agent 1 takes the caller's response and decides where it goes.
    intent = reception_agent.classify(user_response)

    # Dispatch to the specialist agent for that intent.
    if intent == "complaint":
        reply = complaint_agent.run(user_response)
    elif intent == "plan_info":
        reply = plan_info_agent.run()
    elif intent == "new_service":
        reply = new_service_agent.run()
    elif intent == "technical":
        reply = technical_agent.run(user_response)
    elif intent == "billing":
        reply = billing_agent.run()
    else:
        reply = "Sorry, I could not route your request."

    print(f"[reception -> {intent}] {reply}")
    return reply
