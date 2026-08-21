# Commit Message Agent

## Purpose
Given a git diff, writes a single concise commit message summarizing the change.

## Interface
`generate_commit_message(diff: str) -> str`

## Behavior
- Describe *why* the change was made, not just what changed, when that's inferable from the diff.
- Return a single-line summary under 72 characters. No body, no markdown, no trailing period.
- If the diff is empty or whitespace-only, return `"No changes to commit."` without calling the API.

## Model
claude-opus-5
