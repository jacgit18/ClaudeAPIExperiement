import os
import sys

import anthropic
from dotenv import load_dotenv

MODEL = "claude-opus-5"


def main() -> None:
    load_dotenv()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ANTHROPIC_API_KEY is not set. Export it or put it in a .env file.", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic()
    messages: list[dict] = []

    print("Claude CLI chat. Type 'exit' or 'quit' to leave.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            break

        messages.append({"role": "user", "content": user_input})

        try:
            with client.messages.stream(
                model=MODEL,
                max_tokens=4096,
                messages=messages,
            ) as stream:
                print("Claude: ", end="", flush=True)
                for text in stream.text_stream:
                    print(text, end="", flush=True)
                print("\n")
                response = stream.get_final_message()
        except anthropic.APIStatusError as e:
            print(f"\nAPI error: {e.message}", file=sys.stderr)
            messages.pop()
            continue
        except anthropic.APIConnectionError:
            print("\nNetwork error — check your connection.", file=sys.stderr)
            messages.pop()
            continue

        assistant_text = next(
            (block.text for block in response.content if block.type == "text"), ""
        )
        messages.append({"role": "assistant", "content": assistant_text})


if __name__ == "__main__":
    main()
