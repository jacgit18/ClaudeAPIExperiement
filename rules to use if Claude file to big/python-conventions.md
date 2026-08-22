# Python conventions for this project

- No comments unless explaining a non-obvious *why* — names should carry the *what*.
- Type hints on the signature of anything public (functions in `agents/`, `build_agent.py`).
- Catch `anthropic.APIStatusError` / `anthropic.APIConnectionError` specifically —
  never a bare `except Exception` around an API call.
- Every script should run via `./venv/bin/python <script>.py` with no extra setup
  beyond `.env` having a valid `ANTHROPIC_API_KEY`.
