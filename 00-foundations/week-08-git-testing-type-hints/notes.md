# Week 8 Notes — Git, Testing, and Type Hints

## What I learned today

This week wasn't about writing new features, it was about writing code that proves itself, and about using Git properly instead of just as a place to push finished work.

### Type hints — telling Python, and other humans, what a function expects

Up to now, my functions took arguments without saying what type they expected. Type hints are a way to write that expectation directly into the function's signature.

```python
def is_positive(number: float) -> bool:
    return number > 0
```

This says: `number` should be a float, and the function returns a bool. Python does not actually enforce this at runtime, a type hint will not stop someone from passing a string, but it does two real things. It documents intent directly in the code, so anyone reading the function signature knows what's expected without reading the whole body. And it lets tools, like VS Code's Pylance, catch likely mistakes before the code even runs, by underlining a call that clearly passes the wrong type.

```python
from typing import Optional

def find_user(user_id: int) -> Optional[dict]:
    # Optional[dict] means: this returns either a dict, or None
    ...
```

The lesson underneath this: type hints are a form of communication, aimed at the next person reading the code, including future me.

### Writing real tests, not just proving something works once

I already had a few tests from ForgeKit, but this week was about testing properly, not just writing one happy-path test per function.

A good test checks three kinds of cases. The normal case, where everything is as expected. The edge case, where input is at a boundary, empty, zero, exactly at a limit. And the failure case, where bad input should be rejected clearly, not silently accepted.

```python
def test_is_positive_normal_case():
    assert is_positive(5) is True

def test_is_positive_edge_case_zero():
    assert is_positive(0) is False

def test_is_positive_negative_case():
    assert is_positive(-1) is False
```

Each test should test one specific thing, and its name should say exactly what it's checking, so a failing test tells me immediately what broke without having to read the test body.

### Testing that something correctly raises an error

A function that's supposed to reject bad input needs a test proving it actually does. `pytest.raises` checks that a specific exception happens.

```python
import pytest

def test_to_title_case_rejects_wrong_type():
    with pytest.raises(TypeError):
        to_title_case(12345)
```

If `to_title_case` stopped raising `TypeError` for some reason, in a future edit, this test would fail immediately, which is exactly the point, it catches a regression before a client ever sees it.

### Git, beyond init, add, commit, push

I already knew the basic commands, this week was about using them properly. A commit message should describe what changed and, briefly, why, not just say "update" or "fix." Meaningful commit history is itself a form of documentation, useful for me in six months, and useful for a client reviewing what was done and when.

```bash
git log --oneline
```

shows a compact history of commits, useful for quickly scanning what's happened.

```bash
git diff
```

shows exactly what changed in files that haven't been committed yet, useful for reviewing my own work before committing it.

```bash
git branch feature/new-thing
git checkout feature/new-thing
```

A branch is a separate line of work, useful for trying something without touching the main, working version until it's ready. I don't need this constantly on small solo projects, but it matters a lot once client work involves testing a risky change.

### Why testing and Git actually connect

The real link between these two topics this week: a good commit history combined with a real test suite means I can make a change, run the tests, know immediately whether I broke something, and if I did, look back through Git history to see exactly what changed. Without tests, I'd only find out something broke when a client did. Without clean commit history, I'd have a much harder time finding which change caused it.

## What I built

Added type hints across all of ForgeKit's functions. Expanded ForgeKit's test suite to properly cover normal, edge, and failure cases for each function, not just one test per function. Built a new test suite for SentinelCLI's `FileInspector` class, which had zero automated tests before this week despite being a shipped, working project.

## Why this actually matters in real life

This week is directly the difference between "a script that worked when I tried it" and "a project I could hand to a client with confidence." Real client work gets modified over time, new requirements, small fixes, added features. Without tests, every change is a guess about whether something else broke. With tests, every change comes with actual proof. This is also exactly what separates a $50 quick fix from a $300 job the client trusts enough to keep paying for, maintainability, not just working code.