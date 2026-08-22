# Agent spec format

Every file in `specs/` has four sections, in order: Purpose, Interface, Behavior, Model.

`build_agent.py` doesn't validate this structure — a malformed spec still gets sent
to Claude, it just produces worse code. Keep Interface a literal function signature,
not prose, so the generated module's public API stays predictable. Keep Behavior as
bullet points covering edge cases explicitly (empty input, missing config) — those
are the lines that most directly become `if` branches in the generated code.
