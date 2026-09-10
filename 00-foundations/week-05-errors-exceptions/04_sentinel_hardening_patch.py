"""
SentinelCLI

A small command line tool that inspects a file and tells you
what is inside it without requiring you to open it manually.

Supported file types:

    CSV       Reports row count, column count, headers,
              and inconsistent row lengths.

    JSON      Reports whether the data is a list, dictionary,
              or single value, plus basic shape information.

    TXT/LOG   Counts lines and scans for suspicious keywords.

Week 5 focus:

    Defensive programming
    Error handling
    Input validation
    Detecting malformed or inconsistent data

Usage:

    python sentinel.py path/to/file.csv
    python sentinel.py path/to/file.json
    python sentinel.py path/to/file.log
"""

import sys
import csv
import json
import os


# ============================================================
# SETTINGS
# ============================================================

# A SET is used because SentinelCLI repeatedly checks whether
# words belong to this collection.
#
# Sets provide efficient membership testing and also allow
# useful operations such as intersection (&).

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


# ============================================================
# CSV HANDLING
# ============================================================

def analyze_csv(filepath):
    """
    Reads a CSV file and reports its basic structure.

    The function reports:

        Number of data rows
        Number of columns
        Column headers

    It also checks whether every data row has the same number
    of columns as the header.

    Week 5 hardening:
        Handle permission errors.
        Detect inconsistent row lengths.
    """

    try:
        with open(filepath, "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            rows = list(reader)

    except PermissionError:
        print(f"Cannot read this file, permission denied: {filepath}")
        return

    except OSError as e:
        print(f"Could not read the CSV file: {e}")
        return

    # Handle an empty CSV file before trying to access rows[0].
    if not rows:
        print("This CSV file is empty. No headers, no rows.")
        return

    # The first row is treated as the header.
    headers = rows[0]

    # Everything after the header is considered data.
    data_rows = rows[1:]

    # A TUPLE represents the measured shape of the file.
    # Once calculated, we do not need to modify it.
    file_shape = (len(data_rows), len(headers))

    print("File type: CSV")
    print(f"Rows: {file_shape[0]}")
    print(f"Columns: {file_shape[1]}")
    print(f"Headers: {headers}")

    # --------------------------------------------------------
    # WEEK 5 HARDENING
    # --------------------------------------------------------
    # Check whether every data row contains the same number
    # of columns as the header.
    #
    # Before this check, a malformed row could be silently
    # accepted as valid data.

    mismatched = [
        (i + 2, len(row))
        for i, row in enumerate(data_rows)
        if len(row) != len(headers)
    ]

    if mismatched:
        print(
            f"Warning: {len(mismatched)} row(s) have a "
            "different column count than the header:"
        )

        for line_number, column_count in mismatched:
            print(
                f"  Row at line {line_number}: "
                f"{column_count} columns "
                f"(expected {len(headers)})"
            )

    else:
        print("CSV structure looks consistent.")


# ============================================================
# JSON HANDLING
# ============================================================

def analyze_json(filepath):
    """
    Reads a JSON file and reports its basic structure.

    The function identifies whether the top level JSON data
    is a list, dictionary, or single value.

    It also handles:

        Empty files
        Invalid JSON syntax
        File reading errors
    """

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            raw_text = f.read()

    except PermissionError:
        print(f"Cannot read this file, permission denied: {filepath}")
        return

    except OSError as e:
        print(f"Could not read the JSON file: {e}")
        return

    # Handle an empty file before attempting JSON parsing.
    if not raw_text.strip():
        print("This JSON file is empty.")
        return

    try:
        data = json.loads(raw_text)

    except json.JSONDecodeError as e:
        # JSONDecodeError provides useful information about
        # where the parser encountered the problem.
        print("This JSON file is broken and could not be read.")
        print(f"Reason: {e}")
        return

    # --------------------------------------------------------
    # JSON LIST
    # --------------------------------------------------------

    if isinstance(data, list):

        print("File type: JSON (list)")
        print(f"Total items: {len(data)}")

        if data:
            print(
                f"First item type: "
                f"{type(data[0]).__name__}"
            )

            # If the first item is a dictionary, show its keys.
            if isinstance(data[0], dict):
                print(
                    f"Keys in first item: "
                    f"{list(data[0].keys())}"
                )

    # --------------------------------------------------------
    # JSON DICTIONARY
    # --------------------------------------------------------

    elif isinstance(data, dict):

        print("File type: JSON (dictionary)")
        print(f"Top level keys: {list(data.keys())}")

    # --------------------------------------------------------
    # JSON SINGLE VALUE
    # --------------------------------------------------------

    else:

        print(
            "File type: JSON "
            f"(single value: {type(data).__name__})"
        )


# ============================================================
# TEXT / LOG HANDLING
# ============================================================

def analyze_text(filepath):
    """
    Reads a text or log file and scans it for suspicious words.

    The function reports:

        Total number of lines
        Number of suspicious lines
        Suspicious words found on each matching line

    Suspicious keyword matching uses a SET intersection.
    """

    try:
        with open(
            filepath,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:

            lines = f.readlines()

    except PermissionError:
        print(f"Cannot read this file, permission denied: {filepath}")
        return

    except OSError as e:
        print(f"Could not read the text/log file: {e}")
        return

    # Handle an empty text or log file.
    if not lines:
        print("This text/log file is empty.")
        return

    print("File type: TEXT/LOG")
    print(f"Total lines: {len(lines)}")

    # A DICTIONARY stores the findings.
    #
    # Example:
    #
    # {
    #     2: ["timeout"],
    #     5: ["failed", "error"]
    # }
    #
    # The key is the line number.
    # The value is the suspicious words found there.

    findings = {}

    for line_number, line in enumerate(lines, start=1):

        # Convert the line into a SET of words.
        #
        # lower() makes matching case insensitive.
        words_in_line = set(line.lower().split())

        # Set intersection gives us only the words that appear
        # in both the line and the suspicious keyword set.

        matches = words_in_line & SUSPICIOUS_WORDS

        if matches:
            findings[line_number] = list(matches)

    # No suspicious words were detected.
    if not findings:
        print("No suspicious words found.")
        return

    print(f"Suspicious lines found: {len(findings)}")

    for line_number, matches in findings.items():
        print(f"  Line {line_number}: {matches}")


# ============================================================
# FILE TYPE ROUTER
# ============================================================

def detect_and_analyze(filepath):
    """
    Determines the file type from its extension and sends
    the file to the appropriate analyzer.

    The function also handles:

        Missing files
        Missing extensions
        Unsupported extensions
    """

    # Check whether the requested file actually exists.
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    # Separate the filename from its extension.
    _, extension = os.path.splitext(filepath)

    # Normalize the extension so .CSV and .csv behave the same.
    extension = extension.lower()

    if extension == ".csv":

        analyze_csv(filepath)

    elif extension == ".json":

        analyze_json(filepath)

    elif extension in (".txt", ".log"):

        analyze_text(filepath)

    else:

        print(
            "Unrecognized or missing file extension: "
            f"'{extension or '(none)'}'"
        )

        print(
            "Supported types: "
            ".csv, .json, .txt, .log"
        )


# ============================================================
# ENTRY POINT
# ============================================================

def main():
    """
    Main command line entry point.

    SentinelCLI expects exactly one argument:
    the path to the file being inspected.
    """

    if len(sys.argv) != 2:

        print(
            "Usage: "
            "python sentinel.py <path-to-file>"
        )

        sys.exit(1)

    filepath = sys.argv[1]

    detect_and_analyze(filepath)


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()