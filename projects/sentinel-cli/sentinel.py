"""
SentinelCLI — a small command-line tool that inspects a file and tells you
what's inside it, without you having to open it manually.

Supports three file types:
  - CSV   → reports row count, column count, and header names
  - JSON  → reports whether the data is a list or a dictionary, plus shape
  - TXT/LOG → counts lines and scans for suspicious keywords

Usage:
    python sentinel.py path/to/file.csv
    python sentinel.py path/to/file.json
    python sentinel.py path/to/file.log
"""

import sys
import csv
import json
import os

# ── SETTINGS ─────────────────────────────────────────────────
# A SET, not a list — because we're checking "is this word in here?"
# thousands of times as we scan a file. Sets make that check fast,
# no matter how big the set gets. This is the Week 4 collections
# lesson applied for real.
SUSPICIOUS_WORDS = {
    "error",
    "failed",
    "unauthorized",
    "attack",
    "denied",
    "breach",
    "malware",
    "timeout",
}


# ── CSV HANDLING ─────────────────────────────────────────────
def analyze_csv(filepath):
    """
    Reads a CSV file and reports its shape: how many rows, how many
    columns, and what the column headers are.
    """
    with open(filepath, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)  # turn the whole file into a LIST of rows

    if not rows:
        # An empty file — handle it cleanly instead of crashing later
        # when we try to read rows[0].
        print("This CSV file is empty. No headers, no rows.")
        return

    headers = rows[0]          # first row = column names
    data_rows = rows[1:]       # everything after that = the actual data

    # A TUPLE, because this shape shouldn't change once we've measured it.
    file_shape = (len(data_rows), len(headers))

    print(f"File type: CSV")
    print(f"Rows: {file_shape[0]}")
    print(f"Columns: {file_shape[1]}")
    print(f"Headers: {headers}")


# ── JSON HANDLING ────────────────────────────────────────────
def analyze_json(filepath):
    """
    Reads a JSON file and reports whether the top-level data is a
    list or a dictionary, plus some basic shape details.

    JSON files are easy to break by hand (a missing comma, a missing
    bracket) so this function has to handle that gracefully instead
    of letting the whole program crash.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        raw_text = f.read()

    if not raw_text.strip():
        print("This JSON file is empty.")
        return

    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError as e:
        # This is the "broken JSON" case from the notes — catch it,
        # explain what went wrong, and stop cleanly instead of
        # crashing the whole program.
        print("This JSON file is broken and could not be read.")
        print(f"Reason: {e}")
        return

    if isinstance(data, list):
        print(f"File type: JSON (list)")
        print(f"Total items: {len(data)}")
        if data:
            print(f"First item type: {type(data[0]).__name__}")
            # If the list is full of dictionaries, show what keys
            # the first one has — useful for a quick shape check.
            if isinstance(data[0], dict):
                print(f"Keys in first item: {list(data[0].keys())}")

    elif isinstance(data, dict):
        print(f"File type: JSON (dictionary)")
        print(f"Top-level keys: {list(data.keys())}")

    else:
        print(f"File type: JSON (single value: {type(data).__name__})")


# ── TEXT / LOG HANDLING ──────────────────────────────────────
def analyze_text(filepath):
    """
    Reads a text or log file, counts the lines, and scans each line
    for suspicious keywords using the SUSPICIOUS_WORDS set.
    """
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    if not lines:
        print("This text/log file is empty.")
        return

    print(f"File type: TEXT/LOG")
    print(f"Total lines: {len(lines)}")

    # A DICTIONARY to collect findings: line number -> list of words found.
    # This is exactly the "nested data" idea from the notes — a dict
    # that contains, per line, a list of matches.
    findings = {}

    for line_number, line in enumerate(lines, start=1):
        words_in_line = set(line.lower().split())  # a SET of this line's words

        # & gives us only the words that appear in BOTH sets —
        # i.e. the suspicious words actually present on this line.
        matches = words_in_line & SUSPICIOUS_WORDS

        if matches:
            findings[line_number] = list(matches)

    if not findings:
        print("No suspicious words found.")
        return

    print(f"Suspicious lines found: {len(findings)}")
    for line_number, matches in findings.items():
        print(f"  Line {line_number}: {matches}")


# ── FILE TYPE ROUTER ─────────────────────────────────────────
def detect_and_analyze(filepath):
    """
    Looks at the file's extension and sends it to the right analyzer.
    Handles the "no extension at all" case cleanly instead of guessing.
    """
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    _, extension = os.path.splitext(filepath)
    extension = extension.lower()

    if extension == ".csv":
        analyze_csv(filepath)
    elif extension == ".json":
        analyze_json(filepath)
    elif extension in (".txt", ".log"):
        analyze_text(filepath)
    else:
        print(f"Unrecognized or missing file extension: '{extension or '(none)'}'")
        print("Supported types: .csv, .json, .txt, .log")


# ── ENTRY POINT ───────────────────────────────────────────────
def main():
    if len(sys.argv) != 2:
        print("Usage: python sentinel.py <path-to-file>")
        sys.exit(1)

    filepath = sys.argv[1]
    detect_and_analyze(filepath)


if __name__ == "__main__":
    main()