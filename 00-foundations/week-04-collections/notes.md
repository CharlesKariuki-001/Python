<<<<<<< HEAD
# Week 4 Notes
=======
# Week 4 Notes: Collections
>>>>>>> 4f98387 (feat: harden Weeks 1-4 with exception handling and input validation (Week 5))

## What I Learned Today

Today was about **collections**, the different ways Python stores more than one value at a time.

Before this week, I was mostly thinking about one value in one variable. Real programs rarely work that way. They process groups of data such as rows, records, log lines, keywords, and API responses.

Python provides several collection types, and each one is designed for a different problem.

## Lists

A list is an **ordered and changeable** collection that allows duplicates.

Each item has a position called an index. Indexing starts at `0`, not `1`.

```python
suspicious_words = ["error", "failed", "unauthorized", "error"]

print(suspicious_words[0])
# error
```

Use a list when order matters and the collection may need to change.

Lists are useful for things such as CSV rows, log lines, and groups of results.

## Dictionaries

A dictionary stores information using **keys and values**.

Instead of asking for an item by its position, you ask for it using a meaningful label.

```python
row_info = {
    "rows": 120,
    "columns": 5
}

print(row_info["rows"])
# 120
```

One important lesson was the difference between square bracket access and `.get()`.

Using:

```python
row_info["missing_key"]
```

causes an error when the key does not exist.

Using:

```python
print(row_info.get("missing_key"))
# None

print(row_info.get("missing_key", 0))
# 0
```

allows the program to provide a safe fallback.

This matters in real software because input data cannot always be assumed to contain every key we expect.

## Tuples

A tuple is similar to a list, but it **cannot be changed after it is created**.

```python
file_shape = (120, 5)
```

Here the values represent rows and columns.

Tuples are useful when information should remain fixed. Examples include coordinates, fixed configuration values, or data that should not accidentally be modified later.

The important idea is that a tuple provides a level of protection against accidental changes.

## Sets

A set is a collection of **unique values where order is not the main concern**.

Sets are especially useful for membership testing and comparing groups of values.

```python
suspicious_words = {
    "error",
    "failed",
    "unauthorized",
    "attack"
}

found_words = {
    "login",
    "error",
    "success"
}

print(suspicious_words & found_words)
# {'error'}
```

The `&` operator finds the intersection, meaning the values shared by both sets.

Other useful set operations include:

```text
&    intersection
|    union
−    difference
```

The membership operation is also efficient:

```python
if word in suspicious_words:
    print("Suspicious word found")
```

This is why sets were useful in SentinelCLI when checking log lines against a collection of suspicious keywords.

## Comprehensions

A comprehension is a concise way of creating a new collection from an existing one.

The normal approach is:

```python
squares = []

for n in range(5):
    squares.append(n * n)
```

The same operation can be written as:

```python
squares = [n * n for n in range(5)]
```

The pattern:

```python
[expression for item in collection]
```

can be understood as:

> For each item, perform this operation and collect the results.

At first comprehensions were difficult to read, but understanding them as compressed loops made them much easier to understand.

I also learned that shorter code is not automatically better code. If a normal loop is clearer, I would rather use the normal loop.

## Nested Data

Real data is usually more complicated than one simple list or dictionary.

Collections can contain other collections.

For example:

```python
file_report = {
    "filename": "log.txt",
    "issues": [
        {"line": 12, "word": "unauthorized"},
        {"line": 45, "word": "failed"}
    ]
}
```

To access the first suspicious word:

```python
file_report["issues"][0]["word"]
```

This produces:

```text
unauthorized
```

Nested structures are common when working with JSON files, APIs, databases, and other real world data sources.

## What I Built: SentinelCLI

I built **SentinelCLI**, a small Python command line tool that inspects files and reports what is inside them.

For CSV files it reports:

```text
Row count
Column count
Headers
```

For JSON files it reports:

```text
Whether the data is a list or dictionary
Number of items when applicable
Type of the first item
Keys in the first item when applicable
```

For TXT and log files it reports:

```text
Total number of lines
Number of suspicious lines
Suspicious keywords found on each matching line
```

The suspicious keyword set contains:

```text
error
failed
unauthorized
attack
denied
breach
malware
timeout
```

This project gave me a practical reason to use the collections I had just learned.

## Breaking It on Purpose

I deliberately tested SentinelCLI with unexpected input to see how it behaved.

### Empty File

Command:

```text
python sentinel.py samples/empty_file.txt
```

Output:

```text
This text/log file is empty.
```

The program checks whether the file contains content before processing it, so an empty file produces a clear message instead of causing a crash.

### Malformed JSON

Command:

```text
python sentinel.py samples/malformed.json
```

Output:

```text
This JSON file is broken and could not be read.
Reason: Expecting ',' delimiter: line 4 column 1 (char 119)
```

The JSON file was missing its closing structure.

Python's JSON parser detected the problem and reported where it became confused.

My code catches that error with `try` and `except` and gives the user a clear explanation instead of exposing a raw traceback.

The useful part is that the error contains a specific location:

```text
line 4 column 1
```

That gives the person fixing the file somewhere specific to investigate.

### File With No Extension

Command:

```text
python sentinel.py samples/no_extension_file
```

Output:

```text
Unrecognized or missing file extension: '(none)'
Supported types: .csv, .json, .txt, .log
```

Instead of guessing the file type, the program checks the extension and clearly tells the user when it does not recognize it.

## Why This Matters

SentinelCLI is small, but the ideas behind it appear in real software.

Security and data systems regularly process large amounts of information and need to understand the structure of that information before doing anything with it.

Checking whether a value belongs to a collection is a basic operation that becomes important when processing large amounts of data.

Checking file structure before processing it is another practical engineering habit. If the input does not have the expected shape, a system should handle that situation deliberately rather than blindly continuing.

The malformed JSON test also introduced an important software engineering principle:

> Good software should expect bad input and handle it gracefully.

Instead of simply crashing, SentinelCLI explains what went wrong and, when possible, gives useful information about where the problem occurred.

## Main Lessons

The biggest lessons from Week 4 were:

```text
Lists are useful for ordered, changeable collections.

Dictionaries are useful for labelled data.

Tuples are useful for values that should remain fixed.

Sets are useful for unique values, membership testing, and set operations.

Comprehensions provide concise ways to build collections.

Nested collections represent the structure of real world data.

Defensive programming makes software more reliable when input is unexpected.
```

Most importantly, I learned that programming concepts become easier to understand when they are used to solve an actual problem.

SentinelCLI turned collections from something I was only studying into something I could use in a working program.

## Final Reflection

The project also changed how I think about what makes a project useful.

A project starts to feel real when another person can clone the repository, read the documentation, run one command, and understand what the program does without needing me to explain it.

That is the standard I want to keep building toward throughout the Python Forge 180 Day journey.

**Learn the concept. Build something with it. Break it. Understand why it broke. Improve it. Ship it.**
