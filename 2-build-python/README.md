# build-python (2-build-python)

A small multi-agent demo for a **mobile network call center**. A reception
agent takes the caller's response, decides what they need, and the coordinator
routes the call to the right specialist agent. Each agent uses simple shared
tools (a knowledge base and a ticket store).

## Agents

| # | Agent               | Role                                   |
|---|---------------------|----------------------------------------|
| 1 | `reception_agent`   | Takes the caller's response, classifies the intent |
| 2 | `complaint_agent`   | Registers a user complaint (opens a ticket) |
| 3 | `plan_info_agent`   | Returns the caller's current plan info |
| 4 | `new_service_agent` | Lists newly available services         |
| 5 | `technical_agent`   | Technical problem resolution           |
| 6 | `billing_agent`     | Billing and payments                   |

## How the agents coordinate

```
caller text
    │
    ▼
Agent 1 (reception_agent.classify)      ── decides the intent
    │
    ▼
coordinator.run                         ── dispatches to one specialist
    │
    ├── complaint   → Agent 2  → ticket_store
    ├── plan_info   → Agent 3  → knowledge_base
    ├── new_service → Agent 4  → knowledge_base
    ├── technical   → Agent 5  → ticket_store
    └── billing     → Agent 6  → ticket_store
```

The **coordinator** is the single point that knows about every agent. Agent 1
only classifies; it does not call the others. The specialists do not call each
other either — they return a reply to the coordinator, which keeps the design
flat and simple (one hub, many spokes).

## Layout

```
src/build_python/
├── __init__.py
├── main.py                     # entry point (CLI)
├── agents/
│   ├── coordinator.py          # the hub: routes to specialists
│   ├── reception_agent.py      # Agent 1
│   ├── complaint_agent.py      # Agent 2
│   ├── plan_info_agent.py      # Agent 3
│   ├── new_service_agent.py    # Agent 4
│   ├── technical_agent.py      # Agent 5
│   └── billing_agent.py        # Agent 6
└── tools/
    ├── knowledge_base.py       # plans + services lookup
    └── ticket_store.py         # complaints + billing records
```

## Install

```bash
uv sync
```

## Run

```bash
uv run build-python "my internet is slow"
uv run build-python "I want to register a complaint"
uv run build-python "what is my current plan"
uv run build-python "show me new offers"
uv run build-python "I have a billing question"
```

## Develop

```bash
uv run ruff check .      # lint
uv run ruff format .     # format
uv run pytest            # test
```
