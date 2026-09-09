# SentinelCLI

A small command line toolkit that inspects a file (CSV, JSON, or TXT/log) and reports what's inside it. When given a log file, it also flags any lines containing suspicious keywords.

This is the first real flagship project of the Python Forge 180 day build, built after learning lists, dictionaries, tuples, sets, comprehensions, and nested data.

## The Problem

Real world data almost never arrives in a clean, known shape. A CSV might be missing headers. A JSON file might have a stray comma. A log file might have thousands of lines and you need to know, at a glance, which ones actually matter. SentinelCLI is a first, simple pass at that problem: point it at a file, and it tells you what kind of data it's looking at and whether anything looks off.

## Install

No external dependencies required, just Python 3.

```bash
git clone https://github.com/CharlesKariuki-001/Python.git
cd Python/projects/sentinel-cli
```

## Usage

```bash
python sentinel.py <path-to-file>
```

## Examples

Inspecting a log file:
```bash
python sentinel.py samples/sample_log.txt
```
This prints the total line count and flags every line containing a suspicious keyword (error, failed, unauthorized, denied, attack, exception), along with the line number and which keyword matched.

Inspecting a CSV file:
```bash
python sentinel.py samples/sample_data.csv
```
This prints the number of data rows, number of columns, and the header names.

Inspecting a JSON file:
```bash
python sentinel.py samples/sample_data.json
```
This prints whether the top level structure is a list or a dictionary, and either the item count or the key names.

## What I Learned Building This

Lists hold ordered data like CSV rows or log lines. Dictionaries hold labeled data like a JSON object or a single report result. Sets are the right tool for keyword matching, since checking membership in a set is fast and the intersection operator (`&`) makes "which of these words actually appear here" a one line answer instead of a nested loop. Comprehensions are useful for quick transformations, like cleaning up header names, but I kept most of the logic as regular loops where a comprehension would have made the code harder to read, not easier.

## Limitations

The suspicious keyword list is hardcoded and very small, a real system would use a configurable list, weighted scoring, and probably regular expressions instead of exact word matches. It does not currently handle extremely large files efficiently, since `readlines()` loads the whole file into memory at once, a streaming approach would be needed for genuinely huge log files. JSON and CSV inspection only report structure, not content quality, there is no check yet for things like missing values or inconsistent row lengths.

## Breaking It (What I Tried)

An empty file (`samples/empty_file.txt`) is handled gracefully with a clear message instead of a crash. A malformed JSON file (`samples/malformed.json`) is caught and reported as an error instead of crashing the whole program. See `NOTES.md` for the full breakdown of what happened in each case and why.