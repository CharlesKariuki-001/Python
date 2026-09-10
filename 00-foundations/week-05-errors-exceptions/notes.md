# Week 5 Notes — Errors, Exceptions, and Debugging

## What I learned today

Up to this point, my programs worked when I gave them exactly what they expected, and crashed the moment something was off. This week was about the gap between those two outcomes, and how to close it.

### The difference between a bug and an exception

A bug is a mistake in my logic. The program runs, but it gives the wrong answer. An exception is different: it is Python telling me, at the exact moment something breaks, that it cannot continue the way I told it to. A `FileNotFoundError`, a `KeyError`, a `ZeroDivisionError`, these are all exceptions. Python is not being difficult when it raises one; it is refusing to guess and silently produce a wrong result.

### try, except, and why the order matters

The basic shape is simple:

```python
try:
    risky_thing()
except SomeSpecificError:
    handle_it()
```

The important lesson is to catch the specific exception I actually expect, not a bare `except:` that swallows everything. A bare except hides real problems, including problems that have nothing to do with what I was trying to handle, like a typo in my own code.

```python
# Bad — this hides everything, including my own mistakes
try:
    value = int(user_input)
except:
    value = 0

# Good — this only catches what I actually expect
try:
    value = int(user_input)
except ValueError:
    print("That wasn't a valid number.")
    value = 0
```

### else and finally

`else` runs only if the try block succeeded, with no exception. `finally` runs no matter what, exception or not, success or failure. `finally` is for cleanup, like closing a file, that has to happen either way.

```python
try:
    f = open("data.csv")
except FileNotFoundError:
    print("File missing.")
else:
    print("File opened successfully.")
finally:
    print("Done attempting to open the file.")
```

### Raising my own exceptions

Sometimes the built in exceptions do not describe the actual problem. I can raise my own, with a message that explains exactly what went wrong, in terms that make sense for my program.

```python
def load_config(data):
    if "api_key" not in data:
        raise ValueError("Config is missing the required 'api_key' field.")
    return data
```

This matters because a clear, specific error message saves real debugging time later, for me or for anyone else using the code.

### The debugging process, not just the tools

The actual skill this week was less about syntax and more about a repeatable process when something breaks.

First, read the full traceback from the bottom up. The bottom line tells you the actual error. The lines above it tell you the path Python took to get there.

Second, reproduce the failure on purpose, with a small, controlled example, instead of guessing at the fix inside the full program.

Third, isolate where it happens. Add a print statement, or use the debugger, to confirm exactly which line the program's understanding of the data stops matching reality.

Fourth, fix the smallest thing that actually causes the failure, not the first thing that looks suspicious.

Fifth, test the fix against the original failure, and against the cases that were already working, to make sure nothing new broke.

### Defensive programming, the bigger idea

The real lesson underneath all of this is that a program should never trust its input blindly. Every place data enters my program, a file being opened, a value being converted, a key being looked up, is a place something can go wrong that is completely outside my control. Defensive code checks for that, and fails with a clear message instead of crashing with a confusing one.

## What I built

This week I did not build a new project. I went back into my Week 1 through Week 4 builds and hardened them: `analyzer.py`, `risk_classifier.py`, `risk_classifierV2.py`, and `sentinel.py`. Each one now handles bad input with a clear message instead of an unhandled crash.

## Why this actually matters in real life

Every real program a client pays for will eventually be given a file that does not exist, a value that is the wrong type, or data in a shape nobody expected. The difference between a demo and something a business can actually rely on is almost entirely in how it behaves at that exact moment. A crash with a raw traceback looks unfinished and unprofessional. A clear message that explains what went wrong, and what to do about it, looks like something built by someone who thought about the real world, not just the happy path.

This is also directly the Python Code Rescue service from the freelance side of this whole plan: diagnosing exactly this kind of failure, quickly and correctly, is the actual service being sold.