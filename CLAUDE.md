# ProjectOne

A learning project for building Claude-powered Python tools. Two things live here:

1. `main.py` — a minimal streaming chat CLI that talks to Claude directly.
2. A spec-driven "agent factory": markdown specs in `specs/` describe single-purpose
   agents, and `build_agent.py` asks Claude to generate the matching Python module
   into `agents/`.

## Structure

- `main.py` — chat CLI, model `claude-opus-5`, loads `ANTHROPIC_API_KEY` from `.env` via python-dotenv.
- `build_agent.py <spec_name>` — reads `specs/<spec_name>.md`, generates `agents/<spec_name>.py`.
- `specs/` — one markdown file per agent: Purpose, Interface, Behavior, Model. Format in `specs/README.md`.
- `agents/` — generated Python modules. Build output — edit the spec and regenerate rather than hand-editing (see `agents/README.md`).

## Conventions

- Default to `claude-opus-5` unless a task explicitly calls for a cheaper model.
- Secrets live in `.env` (gitignored), never hardcoded.
- New agent: write a spec in `specs/`, run `python build_agent.py <name>`, read the
  generated file back before using it — the generator can drift from the spec on edge cases.

@rules/python-conventions.md
@rules/agent-spec-format.md

## Learning sandbox: Claude Code configuration

The items below are a self-directed exploration of how Claude Code project config
works, filled in with examples relevant to this project. Most of them sit at paths
Claude Code doesn't automatically read yet — each entry notes the real path it would
need for that piece to actually take effect, without changing anything you set up.

| Here | Real path | Concept |
|---|---|---|
| `CLAUDE local.md` | `CLAUDE.local.md` (+ `@CLAUDE.local.md` import + gitignore) | personal, untracked project notes |
| `mcp.json` | `.mcp.json` | project-scoped MCP server config |
| `settings.json` | `.claude/settings.json` | shared permissions/hooks/model config |
| `settings local.json` | `.claude/settings.local.json` | personal, gitignored overrides on top of the above |
| `automated claude skills/` | `.claude/skills/<name>/SKILL.md` | instructions Claude loads by relevance, not by name |
| `manual commands/` | `.claude/commands/<name>.md` | slash commands you invoke explicitly (`/name`) |
| `hooks script runner/` | referenced from `settings.json`'s `hooks` key | scripts that run on tool-use events |
| `rules/` | anywhere — pulled in above via `@rules/...` imports | this one *is* live: real CLAUDE.md `@path` imports |
