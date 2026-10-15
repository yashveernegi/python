# build-python

A small multi-agent demo package. A coordinator calls into agents, which in
turn use tools.

## Layout

```
src/build_python/
├── __init__.py
├── main.py              # entry point
├── agents/
│   ├── coordinator.py
│   ├── research_agent.py
│   └── coding_agent.py
└── tools/
    ├── calculator.py
    └── web_search.py
```

## Install

```bash
uv sync
```

## Run

```bash
uv run build-python
```

## Develop

```bash
uv run ruff check .      # lint
uv run ruff format .     # format
uv run pytest            # test
```
