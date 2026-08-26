# Day 2 Notes

## What I learned
- `if / elif / else` — making decisions based on conditions
- Comparison operators (`>`, `<`, `==`, etc.) as the questions behind every `if`
- Logical operators `and`, `or`, `not` for combining conditions
- `for` loops — repeating over a known list of items
- `range()` — repeating a fixed number of times
- `while` loops — repeating until a condition becomes false (and the risk of infinite loops if the condition never changes)
- `+=` as shorthand for "add to what's already there"
- `.lower()` to normalize text input so "Yes", "yes", "YES" are all treated the same

## What I built
A rule-based risk classifier (`risk_classifier.py`) that takes a transaction amount and two yes/no flags (new recipient, unusual time), calculates a risk score using `if/elif` rules, and prints a final risk level: LOW, MEDIUM, or HIGH.

## Breaking it on purpose
- [ ] Negative amount → _(fill in what happened)_
- [ ] Empty input (just Enter) → crashed with a `ValueError`, same reason as Day 1: `float("")` can't convert empty text to a number
- [ ] Huge number (e.g. 99999999999) → _(did the logic still make sense?)_
- [ ] Typing something other than "yes"/"no" → silently treated as "no" — this is a real weakness, not a crash. A typo or unexpected input doesn't fail loudly, it just quietly assumes the safer answer, which could hide risk in a real system.

## How this connects to real systems
This tiny classifier is a simplified version of what real fraud detection and risk-scoring systems do at their core:

- **Banks and payment processors** (Visa, M-Pesa, PayPal) run every transaction through rule engines like this before it even reaches a human checking amount thresholds, new recipients, odd timing, location mismatches, etc. My `if/elif` chain is a miniature version of that rule engine.
- **The scoring approach** (add points for each risky signal, then bucket into LOW/MEDIUM/HIGH) is the same basic pattern used in real credit scoring and insurance risk models  just with far more signals and statistically weighted points instead of flat `+1`/`+3`.
- **The "silent wrong answer" bug** I found (typos being treated as "no") is exactly the kind of subtle flaw that causes real-world fraud systems to miss things — not because they crash, but because they quietly make the wrong assumption. This is why input validation is such a big deal in production security and fintech code  it's covered later in the roadmap (Week 18: Secure Coding).
- **Loops (`for`/`while`)** are how real systems process not just one transaction but thousands per second  today's script only handles one transaction typed by hand, but the loop concept is exactly what scales this into a system that scans an entire transaction log, which is where Week 4's SentinelCLI project is headed.

