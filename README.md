# ProjectOne

A minimal Python CLI that chats with Claude via the Anthropic API.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # then fill in your key
```

`.env` is loaded automatically via `python-dotenv` — no manual export needed.

## Run

```bash
python main.py
```

Type messages at the `You:` prompt; responses stream back in real time. Type `exit` or `quit` to leave.

## Agent factory

Beyond the chat CLI, this project has a small pattern for growing new
single-purpose agents on demand instead of hand-writing each one:

```
specs/    markdown files — one per agent, describing purpose/interface/behavior
agents/   generated Python modules — build output, not hand-written
build_agent.py   reads a spec, asks Claude to generate the matching module
```

Write a spec in `specs/`, then generate its code:

```bash
python build_agent.py commit_message_agent
```

This reads `specs/commit_message_agent.md` and writes `agents/commit_message_agent.py`.
See `specs/README.md` for the spec format, and `specs/commit_message_agent.md` for a
filled-out example. `agents/commit_message_agent.py` currently ships as a hand-written
placeholder (see the comment at the top of that file) — re-run `build_agent.py` once
your API key has credit to replace it with Claude's actual generated version.
