# Day 1 Notes

## What I learned
- Variables store values (`=` assigns, doesn't compare)
- Core types: `int`, `float`, `str`, `bool`
- `input()` always returns text — has to be converted with `int()` or `float()` before doing math
- f-strings (`f"{value}"`) for clean output
- Basic operators: `+ - * / // % **` and comparisons `== != > < >= <=`

## What I built
A small CLI tool (`analyzer.py`) that asks for income and expenses, then prints:
- Savings (income − expenses)
- Savings rate as a percentage
- Whether the user is saving money (True/False)

## Breaking it on purpose
I tried:
- [ ] Normal numbers → worked as expected
- [ ] Expenses bigger than income → savings went negative, correct
- [ ] Income entered as 0 → didn't crash (handled with a safety check)
- [ ] A letter instead of a number → crashed with a `ValueError`

**What the crash taught me:**

The crash taught me that Python expects the code in my .py file to follow Python syntax. I learned that accidentally putting a Windows file path in my Python code can cause a SyntaxError. Instead of being afraid of errors, I should read the error message because Python tells me the file and line where the problem happened. This taught me that errors are useful because they help me find and understand what went wrong.
