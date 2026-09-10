# Week 6 Notes — Object Oriented Programming (OOP)

## What I learned today

Up to now, my programs have been collections of separate functions that pass data between each other. This week was about a different way to organize code: bundling data and the functions that act on that data together, into one thing called an object.

### Why OOP exists, in plain words

SentinelCLI currently has three separate functions, `analyze_csv`, `analyze_json`, `analyze_text`, that each take a filepath and print a report. They don't share any data between them, and there's nothing stopping me from calling them in the wrong order or forgetting to pass the right filepath to the right one.

A class lets me describe "a thing that inspects a file" as one unit. That thing knows its own filepath, knows what type it is, and has methods, which are just functions that belong to it, for figuring out what's inside.

### Class, object, and the difference between them

A class is a blueprint. It describes what something is and what it can do, but it isn't a real thing yet, it's a description.

```python
class FileInspector:
    def __init__(self, filepath):
        self.filepath = filepath
```

An object, also called an instance, is a real thing built from that blueprint.

```python
inspector = FileInspector("data.csv")
```

`inspector` is now a real object. `FileInspector` is the class it was built from. I can make as many separate `FileInspector` objects as I want, each with its own filepath, and they won't interfere with each other.

### `self`, and why it's in every method

`self` refers to the specific object a method is being called on. It's how a method reaches the data that belongs to that particular object, instead of some global variable shared by everyone.

```python
class FileInspector:
    def __init__(self, filepath):
        self.filepath = filepath

    def show_path(self):
        print(f"Inspecting: {self.filepath}")

inspector_a = FileInspector("a.csv")
inspector_b = FileInspector("b.csv")

inspector_a.show_path()   # Inspecting: a.csv
inspector_b.show_path()   # Inspecting: b.csv
```

Each object keeps its own `self.filepath`, even though they were built from the exact same class.

### `__init__`, the setup method

`__init__` runs automatically the moment an object is created. This is where I set up whatever the object needs to know about itself from the start, in SentinelCLI's case, the filepath and the file's extension.

### Inheritance, briefly

A class can be built as a more specific version of another class, inheriting its behavior and adding or changing some of it. I didn't need this for SentinelCLI, since I don't have multiple, meaningfully different kinds of inspector, but the idea matters for later, more complex projects, where a `CSVInspector` and a `JSONInspector` might both inherit shared behavior from a common `FileInspector` base.

### Why this actually helped SentinelCLI

Before this week, `detect_and_analyze` had to figure out the file type and then call the right loose function. Now, a `FileInspector` object can know its own type as soon as it's created, and expose one clean method, `.analyze()`, that does the right thing internally. Anyone using this tool from the outside doesn't need to know there are three different functions underneath, they just create an inspector and call one method.

## What I built

I refactored SentinelCLI from a set of separate functions into a `FileInspector` class. The functionality is identical to before, CSV, JSON, and text/log inspection, plus everything from the Week 5 hardening pass, permission errors and CSV row mismatches included, but it's now organized as one object instead of scattered functions.

## Why this actually matters in real life

Real client projects almost never stay small. A tool that starts as three functions can genuinely, quickly grow into fifteen. Classes are how professional codebases stay readable as they grow, because related data and behavior live together instead of being spread across a file with no clear ownership. This is also exactly the kind of structural improvement a client is paying for when they hire someone for a "Python Code Rescue" job, not just a bug fix, but code that will still make sense to work with six months later.