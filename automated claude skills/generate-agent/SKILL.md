---
name: generate-agent
description: Scaffold a new spec-driven agent for ProjectOne — writes a markdown spec in specs/ and runs build_agent.py to generate the Python module in agents/. Use when the user wants a new single-purpose Claude agent added to this project.
---

# Generate Agent

Given a plain-language description of what the new agent should do:

1. Write a new file `specs/<snake_case_name>.md` following the format in
   `specs/README.md`: Purpose, Interface (a literal function signature), Behavior
   (bullet rules including edge cases), Model.
2. Run `python build_agent.py <snake_case_name>` to generate `agents/<snake_case_name>.py`.
3. Read the generated file back and check it against the spec before telling the
   user it's done — the generator can drift on edge cases.
4. If `build_agent.py` fails with a billing/credit error, report it — it won't
   self-resolve by retrying.
