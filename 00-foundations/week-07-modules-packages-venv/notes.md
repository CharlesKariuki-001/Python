# Week 7 Notes — Modules, Packages, and Virtual Environments

## What I learned today

Every project so far has been one file. SentinelCLI, even after being refactored into a class, still lives in a single sentinel.py. This week was about what happens once one file isn't enough, and how Python actually keeps separate projects from interfering with each other on the same computer.

### A module is just a file

Any Python file is a module. The moment I write `import something`, I am telling Python to go find a file called something.py and make everything inside it available to me.

```python
# validators.py
def is_positive(number):
    return number > 0
```

```python
# main.py
import validators

print(validators.is_positive(5))
```

`main.py` did not need to know how `is_positive` was written internally, only that it exists inside `validators`. This is the same idea as calling a method on an object, applied at the level of whole files.

### A package is a folder of modules

Once I have several related modules, I can group them into a folder. That folder becomes a package the moment it contains a file named `__init__.py`, even if that file is empty.

forgekit/
init.py
validators.py
formatters.py
file_tools.py


`__init__.py` is what tells Python "treat this folder as one importable thing," not just a folder that happens to contain Python files.

### Different ways to import, and why the difference matters

```python
import forgekit.validators
forgekit.validators.is_positive(5)

from forgekit import validators
validators.is_positive(5)

from forgekit.validators import is_positive
is_positive(5)
```

All three do the same thing, but they read differently. The first two keep it clear which module a function came from, which matters once a project has many similarly named functions across different files. The third is convenient for something used constantly, but can get confusing in a large file if I import many things this way and forget where each one came from.

### `__name__ == "__main__"`, what it actually does

Every Python file has a built in variable called `__name__`. When a file is run directly, `__name__` equals `"__main__"`. When that same file is imported by another file instead, `__name__` equals the module's own name.

```python
def main():
    print("Running directly")

if __name__ == "__main__":
    main()
```

This means a file can be built so that running it directly does something, like a demo or a test, but importing it from elsewhere does not accidentally trigger that same thing. Every project I have built so far already uses this pattern without me fully understanding why until now.

### Virtual environments, the actual reason they exist

Different projects often need different versions of the same library. If everything installed on my computer lived in one shared place, one project's needs could quietly break another project that expects an older version of the same package.

A virtual environment is a separate, isolated folder of installed packages, created just for one project.

```bash
python -m venv .venv
```

Activating it points my terminal at that isolated folder instead of the computer's shared Python installation, so anything I `pip install` while it is active only affects this one project.

```bash
source .venv/bin/activate      # Mac/Linux
.venv\Scripts\activate         # Windows
```

`requirements.txt` is the record of exactly what a project needs, so the same environment can be recreated on any machine, including a fresh clone from GitHub.

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```

### Why ForgeKit needed this and SentinelCLI didn't

SentinelCLI is small enough that one file was genuinely fine for it. ForgeKit is different on purpose, it's a toolkit, a collection of small, reusable utilities that don't naturally belong to one single script. Splitting it into separate modules, validators, formatters, file tools, means each piece can be understood, tested, and reused on its own, instead of scrolling through one long file to find the one function I actually need.

## What I built

ForgeKit, a small Python package with three modules: `validators.py`, `formatters.py`, and `file_tools.py`, tied together with an `__init__.py`, plus a `demo.py` that imports and uses functions from all three to prove the package works as a whole.

## Why this actually matters in real life

Every real client project that goes beyond a single script needs this. A FastAPI backend, for instance, is never one file, it's routes, models, validation, and database logic, each in their own module, imported into a main application file. Understanding modules, packages, and virtual environments is not a side skill, it's the actual shape that professional Python projects take, including the API/webhook automation service this whole plan is built around selling.