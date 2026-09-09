# Day 3 Notes

## What I learned
- Functions are named, reusable blocks of code defined with `def`
- Parameters are placeholders for input; arguments are the actual values passed in when calling
- `return` hands a value back to the caller, unlike `print()` which only displays it
- Default arguments make a parameter optional by giving it a fallback value
- Scope - a variable created inside a function only exists inside that function (local scope)
- Breaking one long script into small single-purpose functions makes code easier to read, test, and fix

## What I built
Rebuilt the Day 2 risk classifier so every piece of logic is its own function:
- `get_amount_score()` - scores the transaction amount
- `get_flag_score()` - scores the new-recipient and unusual-time flags
- `get_risk_level()` - converts the total score into LOW/MEDIUM/HIGH
- `main()` - ties everything together and is the only part that actually runs

## Breaking it on purpose
- Called `get_amount_score()` with no arguments - _(fill in the exact error message)_
- Called `get_amount_score(None)` - _(fill in what happened - likely a TypeError comparing None to a number)_
- Called `get_amount_score("500")` - _(fill in - did it crash, or silently misbehave?)_
- Tried printing a variable from inside a function, outside of it - _(fill in the scope error)_

## How this connects to real systems
- Every real production codebase  a fraud engine, a web backend, an ML pipeline  is built from small functions like this, not one giant script. Breaking Day 2's classifier into functions is the actual shape of real engineering work.
- Separating `get_amount_score()`, `get_flag_score()`, and `get_risk_level()` means each rule can be tested and fixed independently if the amount-scoring logic is wrong, I can fix just that function without touching the others. This is exactly how real risk engines at banks and payment companies are structured, just with far more rules per function.
- `return` instead of `print()` matters a lot in real systems. A fraud API doesn't want to "print" a risk score to a screen, it needs to return that score as data so another part of the system (a database, a dashboard, an alert) can use it. This is the exact difference between a toy script and a piece of a real pipeline.
- Scope is what keeps large systems from breaking each other. Imagine hundreds of functions written by different engineers; scope guarantees one function's internal variables can't silently corrupt another's, the same way one microservice shouldn't be able to reach into another's private memory.
- This function-based structure is also what makes Week 8's testing possible later in the roadmap  you can't easily write an automated test for one giant block of code, but you can write one test per function, checking each piece in isolation.
