## Refactor Note (Week 6 — OOP)

This project was originally built as three separate functions. In Week 6, it was refactored into a `FileInspector` class — one object that knows its own filepath and extension, with a single public method, `.analyze()`, that internally routes to the right private method (`_analyze_csv`, `_analyze_json`, `_analyze_text`).

The behavior is identical to the original version; only the structure changed. This is what "refactoring" actually means: improving how code is organized without changing what it does. As this tool (or any tool like it) grows, keeping related data and logic bundled inside one class keeps the code easier to extend and reason about than a growing pile of loose functions.