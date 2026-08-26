#!/usr/bin/env bash
# Example PostToolUse hook: syntax-checks a .py file right after Claude edits it.
# Claude Code hooks receive the tool-call as JSON on stdin (fields include
# tool_name and tool_input); exit code 2 feeds stderr back to Claude as blocking
# feedback instead of silently letting the edit stand. Schema may evolve —
# check the current Claude Code hooks docs before relying on this in a real setup.
set -euo pipefail

file_path=$(jq -r '.tool_input.file_path // empty')

if [[ "$file_path" == *.py ]]; then
  if ! python3 -m py_compile "$file_path" 2>/tmp/syntax_error.txt; then
    echo "Syntax error in $file_path:" >&2
    cat /tmp/syntax_error.txt >&2
    exit 2
  fi
fi
