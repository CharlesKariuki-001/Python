# SentinelCLI

> A lightweight Python command-line toolkit for inspecting CSV, JSON, and TXT/log files  with a simple suspicious-keyword scanner for logs.

**SentinelCLI** is the first flagship project in the **Python Forge 180-Day Build**.

It was built after studying Python collections and nested data structures, including:

* Lists
* Dictionaries
* Tuples
* Sets
* Comprehensions
* Nested data

The goal is simple: **point SentinelCLI at a file and quickly understand what is inside it.**

---

## What SentinelCLI Does

SentinelCLI accepts a file path and determines what kind of data it contains.

It currently supports:

| File Type     | What SentinelCLI Reports                              |
| ------------- | ----------------------------------------------------- |
| CSV           | Row count, column count, and headers                  |
| JSON          | Data structure, item count, first-item type, and keys |
| TXT / Log     | Line count and suspicious lines                       |
| Unknown files | Reports the file as unrecognized                      |

For log files, SentinelCLI performs an additional keyword scan and identifies lines containing potentially suspicious terms.

---

## The Problem

Real-world data rarely arrives in a perfectly known or predictable shape.

A CSV file might have unexpected headers.

A JSON file might be malformed because of a missing bracket or comma.

A log file might contain thousands of lines, making it difficult to immediately identify the entries that deserve attention.

SentinelCLI is a small first step toward solving that problem:

> **Give it a file. It tells you what it is, what's inside it, and for logs whether anything looks suspicious.**

This is intentionally a simple tool. The purpose of the project is not to replace production data-analysis or security platforms, but to demonstrate practical Python fundamentals through a working command-line application.

---

## Project Structure

```text
sentinel-cli/
│
├── sentinel.py
│
├── samples/
│   ├── sample_data.csv
│   ├── sample_data.json
│   └── samples_log.txt
│
└── README.md
```

The project is kept intentionally small so that the Python logic remains easy to understand and inspect.

---

## Requirements

* Python 3
* No external Python dependencies

Everything is built using Python's standard library.

---

## Installation

Clone the Python Forge repository:

```bash
git clone https://github.com/CharlesKariuki-001/Python.git
```

Move into the SentinelCLI project:

```bash
cd Python/projects/sentinel-cli
```

No package installation is required.

---

## Usage

Run SentinelCLI by providing the path to a file:

```bash
python sentinel.py <path-to-file>
```

For example:

```bash
python sentinel.py samples/samples_log.txt
```

---

# Examples

## 1. Inspecting a Log File

Command:

```bash
python sentinel.py samples/samples_log.txt
```

Example output:

```text
File type: TEXT/LOG

Total lines: 6

Suspicious lines found: 3

Line 2: ['timeout']
Line 3: ['unauthorized']
Line 5: ['failed']
```

SentinelCLI checks each line against its suspicious-keyword set and reports which keywords were detected.

---

## 2. Inspecting a CSV File

Command:

```bash
python sentinel.py samples/sample_data.csv
```

Example output:

```text
File type: CSV

Rows: 4
Columns: 3

Headers: ['name', 'age', 'country']
```

The CSV inspection focuses on the basic structure of the file rather than attempting to perform full data-quality analysis.

---

## 3. Inspecting a JSON File

Command:

```bash
python sentinel.py samples/sample_data.json
```

Example output:

```text
File type: JSON (list)

Total items: 3

First item type: dict

Keys in first item: ['user', 'action', 'status']
```

This helps demonstrate how Python handles nested JSON structures and how dictionaries and lists commonly appear when working with structured data.

---

# Suspicious Keyword Detection

For log files, SentinelCLI currently checks each line against the following keyword set:

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

The keywords are stored as a Python `set`.

For example:

```python
SUSPICIOUS_KEYWORDS = {
    "error",
    "failed",
    "unauthorized",
    "attack",
    "denied",
    "breach",
    "malware",
    "timeout",
}
```

Using a set makes membership testing straightforward:

```python
if word in SUSPICIOUS_KEYWORDS:
    ...
```

The tool can then identify which suspicious terms appear on a particular line.

---

# What I Learned

SentinelCLI was primarily a practical exercise in applying Python collections to a real problem.

## Lists

Lists are useful for ordered data.

For example:

* CSV rows
* Log lines
* JSON arrays
* Collections of detected keywords

A list preserves the order of its elements, which is useful when processing files line by line.

---

## Dictionaries

Dictionaries are useful for labelled information.

For example, a JSON object might look conceptually like:

```python
{
    "user": "alice",
    "action": "login",
    "status": "failed"
}
```

Each value is associated with a meaningful key.

This also makes dictionaries useful for representing structured results produced by a program.

---

## Sets

Sets were particularly useful for the suspicious-keyword scanner.

Instead of repeatedly searching through a list of keywords, a set provides a natural way to ask:

```text
Is this word one of the suspicious keywords?
```

The intersection operator also provides a concise way to identify matching terms:

```python
found = words & SUSPICIOUS_KEYWORDS
```

Conceptually, this means:

> "Which words from this line are also in my suspicious-keyword set?"

---

## Comprehensions

Comprehensions are useful for concise transformations and filtering.

However, I deliberately did not use comprehensions everywhere.

One of the lessons from this project was that **shorter code is not automatically better code**.

If a normal loop makes the logic easier to understand, I prefer the normal loop.

The goal is readable Python, not code that is unnecessarily compressed.

---

# Defensive Coding

One of the most valuable lessons from SentinelCLI was learning that input cannot simply be trusted.

A file may look correct but still contain unexpected data.

For example, JSON parsing can fail because of a missing bracket, comma, or other formatting problem.

Instead of allowing the entire application to crash with a raw traceback, SentinelCLI catches the relevant parsing failure and reports a clearer error.

This introduced an important engineering principle:

> **Programs should expect bad input and handle it deliberately.**

---

# Breaking It

I deliberately tested SentinelCLI against several situations that could cause problems.

## Empty File

An empty file is handled gracefully.

Instead of crashing, the program reports that there is no usable content to inspect.

---

## Malformed JSON

A JSON file with invalid syntax, such as a missing bracket or comma, is caught and reported as a clear parsing error.

The application does not simply expose an unhandled traceback to the user.

---

## File With No Extension

A file without a recognizable extension is reported as unrecognized.

SentinelCLI does not attempt to blindly guess the file type.

---

## Larger File

A larger file was also used as a basic sanity check.

The test helped expose an important limitation of the current implementation: although the program can process a larger file, it currently reads the file into memory rather than processing it as a stream.

That distinction matters when moving from small learning projects to genuinely large datasets.

---

# Limitations

SentinelCLI is intentionally a small learning project, so it has several limitations.

### 1. Hardcoded Keywords

The suspicious keyword list is currently hardcoded.

A more mature implementation would allow the keyword list to be configured externally.

---

### 2. Simple Keyword Matching

The scanner currently relies on basic keyword matching.

A production-oriented security analysis system could use more sophisticated techniques, such as:

* Regular expressions
* Pattern matching
* Weighted scoring
* Context-aware detection
* Statistical analysis
* Machine-learning models

SentinelCLI does not attempt to provide those capabilities.

---

### 3. Memory Usage

The current implementation reads file content into memory.

That is acceptable for a small learning project, but it is not ideal for extremely large files.

A more scalable implementation would process data incrementally.

For example, logs could be processed line by line rather than loading the entire file at once.

---

### 4. Limited CSV Validation

CSV inspection currently focuses on basic structure:

* Number of rows
* Number of columns
* Headers

It does not perform deeper data-quality checks such as:

* Missing values
* Inconsistent row lengths
* Invalid data types
* Duplicate records

---

### 5. Limited JSON Validation

JSON inspection focuses primarily on structure.

It does not currently perform deeper analysis of:

* Missing fields
* Unexpected types
* Schema consistency
* Duplicate or invalid values

---

# What I Would Build Next

If SentinelCLI were continued beyond the current learning milestone, the next improvements would be:

```text
1. Configurable suspicious keywords
            ↓
2. Better command-line arguments
            ↓
3. Streaming large log files
            ↓
4. Regular-expression detection
            ↓
5. Severity scoring
            ↓
6. Structured JSON output
            ↓
7. Automated tests
            ↓
8. Logging and error reporting
```

Eventually, it could evolve from a simple file inspector into a more capable **data and security analysis CLI**.

For now, the priority is understanding the fundamentals behind each feature rather than adding complexity for its own sake.

---

# Connection to the Python Forge

SentinelCLI is part of the broader **Python Forge 180-Day Build**.

The progression is intentional:

```text
Python Fundamentals
        ↓
Collections & Data Structures
        ↓
SentinelCLI
        ↓
Software Engineering
        ↓
Data Engineering
        ↓
Machine Learning
        ↓
Larger Engineering Projects
```

Each project is meant to turn a recently learned concept into something usable.

The objective is not simply to complete Python exercises.

The objective is to gradually learn how to **build, test, explain, and improve software.**

---


# Learning Evidence

SentinelCLI demonstrates practical understanding of:

* Python variables and data types
* Lists
* Dictionaries
* Tuples
* Sets
* Set operations
* Comprehensions
* Loops
* Conditional logic
* File handling
* CSV processing
* JSON parsing
* Exception handling
* Basic command-line interfaces
* Defensive programming
* Input validation
* Basic security-oriented pattern detection

More importantly, the project demonstrates the ability to take a Python concept and apply it to a small, working system.

---

# Related Python Forge Work

The next projects in the Python Forge progression will build on the same foundation:

| Project          | Focus                                               |
| ---------------- | --------------------------------------------------- |
| **SentinelCLI**  | File inspection and basic log analysis              |
| **ForgeKit**     | Software engineering and reusable Python tooling    |
| **DataForge**    | Data processing and analysis                        |
| **AnomalyForge** | Machine-learning and anomaly-detection fundamentals |

Each project increases the level of engineering complexity while keeping the learning progression understandable.

---

# License

This project is part of my personal Python engineering learning journey and portfolio.

See the repository license for usage terms.

---

## Author

**Charles Kariuki**

Python Engineering • Cybersecurity • AI Security Engineering

---

> **Build small. Understand deeply. Ship consistently.**
>
> **Python Forge, 180 days of turning knowledge into working software.**
