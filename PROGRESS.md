# Weekly Progress Log

This tracks what's actually been built and shipped, week by week, against the corrected 4-Month Grind roadmap. Only checked items are genuinely done and pushed.

## Week 0 (Sept 9–13) — Setup
- [x] Python, VS Code, Git installed and confirmed working
- [x] GitHub account active with 2FA
- [x] `Python` repo created, folder skeleton built (`00-foundations/`, `01-software-engineering/`, `02-data-engineering/`, `03-machine-learning/`, `comprehension-log/`, `projects/`)
- [x] Root files finished: README, ROADMAP, PROGRESS, LICENSE, CONTRIBUTING, .gitignore
- [x] Structured repo shipped to GitHub
- [x] `Python-Automation` repo also set up in parallel (freelance storefront, separate repo)

## Week 1 (Sept 14–20) — Variables, Types, I/O
Theme: Variables, types, I/O
Ship target: `00-foundations/week-01-building-Blocks/`
- [x] `analyzer.py` built
- [x] `NOTES.md` written
- [ ] Hardened against bad input — scheduled for Week 5 hardening pass

## Week 2 (Sept 21–27) — Conditions and Loops
Theme: Conditions and loops
Ship target: `00-foundations/week-02-decisions-and-loops/`
- [x] `risk_classifier.py` built
- [x] `notes.md` written
- [x] `practice.py` completed
- [ ] Hardened against bad input — scheduled for Week 5 hardening pass

## Week 3 (Sept 28–Oct 4) — Functions
Theme: Functions
Ship target: `00-foundations/week-03-functions/`
- [x] `risk_classifierV2.py` built
- [x] `notes.md` written
- [x] `practice.py` completed
- [ ] Hardened against bad input — scheduled for Week 5 hardening pass

## Week 4 (Oct 5–11) — Collections
Theme: Collections
Ship target: `projects/sentinel-cli/` — DONE
- [x] Lists, dicts, tuples, sets, comprehensions, nested data — `notes.md`
- [x] `practice.py` — all six concepts exercised
- [x] SentinelCLI built — CSV / JSON / text-log analysis
- [x] Break-it tests: empty file, malformed JSON, no extension — real output captured and documented
- [x] README written and verified against real terminal output
- [x] Committed and pushed to GitHub

## Week 5 (Oct 12–18) — Errors, Exceptions, Debugging
Theme: Errors, exceptions, debugging
Ship target: Weeks 1–4 hardened (no new project this week)
- [x] `notes.md` written
- [x] `practice.py` completed
- [x] `analyzer.py` (Week 1) hardened — numeric input validation, negative-value check
- [x] `risk_classifier.py` (Week 2) hardened — numeric validation, strict yes/no parsing
- [x] `risk_classifierV2.py` (Week 3) hardened — same fixes applied across its function structure
- [x] `sentinel.py` (Week 4) extended — PermissionError handling, CSV row/header mismatch warning
- [ ] Comprehension Log entry — deferred, handled separately alongside VigilantAI work

## Week 6 (Oct 19–25) — Object Oriented Programming
Theme: OOP
Ship target: SentinelCLI refactor
- [x] `notes.md` written — classes, objects, self, __init__, inheritance overview
- [x] `practice.py` completed — Transaction, Counter, RiskChecker, RunningTotal, SimpleFileInspector
- [x] `sentinel.py` refactored into a `FileInspector` class
- [x] Verified identical behavior against all Week 4/5 sample files
- [x] README updated with refactor note

## Week 7 (Oct 26–Nov 1) — Modules, Packages, venv
Theme: Modules, packages, venv
Ship target: `projects/forgekit/`
- [x] `notes.md` written — modules, packages, __init__.py, imports, __name__ == "__main__", venv
- [x] `practice.py` completed
- [x] ForgeKit package built — validators, formatters, file_tools modules
- [x] `demo.py` verified working — imports package correctly from outside
- [x] `conftest.py` added to fix pytest's ModuleNotFoundError
- [x] All 6 tests passing
- [x] README written


| Week | Theme | Status |
|---|---|---|
| 0 | Setup | Complete |
| 1 | Variables, types, I/O | Built and hardened |
| 2 | Conditions and loops | Built and hardened |
| 3 | Functions | Built and hardened |
| 4 | Collections — SentinelCLI | Complete and shipped |
| 5 | Errors, exceptions, debugging | Complete |
| 6 | OOP — SentinelCLI refactor | Complete |
| 7 | Modules, packages, venv — ForgeKit | Complete |
---
