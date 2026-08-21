# Specs

Each file here describes one agent: its purpose, its function interface, and the
rules it should follow. `build_agent.py <name>` reads `<name>.md` and asks Claude
to generate the matching Python module in `../agents/<name>.py`.

Write a spec the way you'd brief a contractor — purpose, interface, edge cases.
The more precise the spec, the less you'll need to hand-edit the generated code.

## Format

```markdown
# <Agent Name>

## Purpose
One or two sentences on what the agent does.

## Interface
The function signature it should expose.

## Behavior
Bullet-point rules: what to do, what to return, how to handle edge cases.

## Model
Which Claude model it should call (defaults to claude-opus-5 if omitted).
```

See `commit_message_agent.md` for a filled-out example.
