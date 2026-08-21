import os
import re
import sys

import anthropic
from dotenv import load_dotenv

MODEL = "claude-opus-5"
SPECS_DIR = "specs"
AGENTS_DIR = "agents"

BUILDER_SYSTEM_PROMPT = """You are a code generator. You will be given a markdown \
specification for a single-purpose Claude-powered agent. Generate one self-contained \
Python module that implements it.

Rules:
- Use the `anthropic` SDK (`import anthropic`), matching the style of this project's \
main.py: a module-level MODEL constant, an `anthropic.Anthropic()` client, and typed \
error handling for anthropic.APIStatusError / anthropic.APIConnectionError.
- Expose exactly the public function named in the spec's Interface section, with that \
exact signature.
- Load ANTHROPIC_API_KEY from the environment; assume python-dotenv's load_dotenv() \
has already been called by the caller — don't call it yourself.
- No explanatory prose outside the code. Respond with a single ```python fenced code \
block and nothing else.
"""


def build_agent(spec_name: str) -> None:
    spec_path = os.path.join(SPECS_DIR, f"{spec_name}.md")
    if not os.path.isfile(spec_path):
        print(f"No spec found at {spec_path}", file=sys.stderr)
        sys.exit(1)

    with open(spec_path, "r") as f:
        spec_text = f.read()

    client = anthropic.Anthropic()

    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=8192,
            system=BUILDER_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": spec_text}],
        )
    except anthropic.APIStatusError as e:
        print(f"API error: {e.message}", file=sys.stderr)
        sys.exit(1)
    except anthropic.APIConnectionError:
        print("Network error — check your connection.", file=sys.stderr)
        sys.exit(1)

    text = next((block.text for block in response.content if block.type == "text"), "")
    match = re.search(r"```python\n(.*?)```", text, re.DOTALL)
    code = match.group(1) if match else text

    os.makedirs(AGENTS_DIR, exist_ok=True)
    out_path = os.path.join(AGENTS_DIR, f"{spec_name}.py")
    with open(out_path, "w") as f:
        f.write(code)

    print(f"Generated {out_path}")


if __name__ == "__main__":
    load_dotenv()

    if len(sys.argv) != 2:
        print("Usage: python build_agent.py <spec_name>", file=sys.stderr)
        print(f"Available specs: {', '.join(sorted(f[:-3] for f in os.listdir(SPECS_DIR) if f.endswith('.md') and f != 'README.md'))}", file=sys.stderr)
        sys.exit(1)

    build_agent(sys.argv[1])
