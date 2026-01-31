# Copilot / AI agent instructions — LeetCode solutions repo

Purpose: help AI coding agents quickly become productive in this repository of LeetCode solutions (Python). Keep changes small, predictable and consistent with existing file patterns.

What this repo is
- A personal LeetCode solutions collection organized by topic folders (e.g. `Backtracking`, `DP`, `Tree`, `Trie`, etc.).
- Each problem usually lives in a folder named `<id>. <title>` with two files: a `README.MD` (Chinese + English statement, idea) and a `<id>.py` solver.
- Solutions are Python scripts, runnable directly with `python path/to/file.py`.

High-level guidance for edits
- Preserve folder and file naming conventions: do not rename problem folders (they follow `<id>. <title>`). Update only contents unless the user requests refactoring.
- Do not remove or rewrite bilingual README contents; add English clarifications only if missing.
- Keep each problem file self-contained. Avoid introducing new project-wide dependencies (no new packages) unless the user approves.

Key project patterns to follow
- Uniform backtracking template: many Backtracking solutions use consistent names `res`, `path` (or `selected`), and helper `dfs`/`bk(start)`. When adding/ fixing backtracking code, reuse these names and the append/recurse/pop structure.
  - Example reference: `Backtracking/78. 子集/78.py` and `Backtracking/README.md`.
- I/O style: solutions print simple example outputs in `if __name__ == '__main__':` blocks. Keep those minimal and use them for quick smoke tests.
- README.md usage: per-problem `README.MD` holds the English problem statement, examples and constraints — prefer adding missing examples there.

Development workflows (what to run)
- Run a single problem file locally:

```bash
python Backtracking/78. 子集/78.py
```

- Run quick multi-file smoke tests from repository root using Python's `runpy` (used by the agent in this repo): implement small runner scripts or use `python -c` with `runpy.run_path`.

Repository-specific conventions
- Variable names: maintain `res`, `path`, `dfs`/`bk`, `start`, `used` for permutations, `remain` for remaining target in combinationSum. This keeps the code uniform for the repo owner.
- README content: keep both Chinese explanation and an English paraphrase with Examples + Constraints.

What to avoid
- Don't introduce new package managers or dependency files (`requirements.txt`, `pyproject.toml`) without asking — this repository intentionally keeps solutions runnable with the system Python.
- Avoid sweeping renames or auto-formatting that touch many files; owner prefers small, focused edits.

Integration points and external dependencies
- There are no external services or complex integrations — pure Python solutions only.
- Git branches: user works with `master` locally; prefer committing to `master` unless asked otherwise.

Examples of actionable tasks for AI agents
- Add or repair a missing solution implementation following the repository's naming/template conventions.
- Add English problem statements and examples to `README.MD` if absent, using existing language style.
- Create small test snippets in `if __name__ == '__main__':` that demonstrate expected outputs for sample inputs.

If uncertain, ask these targeted questions
- "Do you want me to add a new dependency?" (avoid new deps unless user agrees)
- "Should I refactor filenames or keep the current `<id>. <title>` naming?" (default: keep)
- "Push the commit to remote?" (agent will not push without explicit permission)

Finish: after updating files, run small smoke tests for the changed problems and report results. Ask for feedback and clarify any preferred stylistic changes.
