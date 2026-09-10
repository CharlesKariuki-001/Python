"""
SentinelCLI — a small command-line tool that inspects a file and reports
what is inside it without requiring the user to open it manually.

Week 6 OOP Refactor:
    SentinelCLI has been reorganized from separate analysis functions
    into a FileInspector class.

Supported file types:
    CSV      → reports rows, columns, headers, and row inconsistencies
    JSON     → reports list, dictionary, or single-value structure
    TXT/LOG  → counts lines and scans for suspicious keywords

Week 5 hardening retained:
    Defensive programming
    File existence validation
    Permission error handling
    File reading error handling
    CSV structure validation
    Invalid JSON handling
    Empty file handling

Week 6 OOP concepts applied:
    Class
    Object
    self
    __init__
    Instance attributes
    Methods
    Encapsulation
    Public method
    Internal/private methods by convention

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
# FILE INSPECTOR CLASS
# ============================================================

class FileInspector:
    """
    Represents one file that SentinelCLI is going to inspect.

    The object stores the filepath and its extension as instance
    attributes. The public analyze() method decides what type of
    analysis is required, while the internal analysis methods
    perform the actual work.

    This structure applies the Week 6 OOP lesson by keeping
    related data and behavior together.
    """

    def __init__(self, filepath):
        """
        Set up a FileInspector object.

        self.filepath:
            Stores the path belonging to this particular object.

        self.extension:
            Stores the normalized file extension.
        """
        self.filepath = filepath

        _, extension = os.path.splitext(filepath)
        self.extension = extension.lower()

    # ========================================================
    # PUBLIC METHOD
    # ========================================================

    def analyze(self):
        """
        Analyze the file using the appropriate internal method.

        This is the main public method of the FileInspector class.
        Code using the class does not need to know whether the
        file is CSV, JSON, TXT, or LOG.
        """

        # ----------------------------------------------------
        # FILE EXISTENCE VALIDATION
        # ----------------------------------------------------

        if not os.path.exists(self.filepath):
            print(f"File not found: {self.filepath}")
            return

        # ----------------------------------------------------
        # FILE TYPE ROUTING
        # ----------------------------------------------------

        if self.extension == ".csv":
            self._analyze_csv()

        elif self.extension == ".json":
            self._analyze_json()

        elif self.extension in (".txt", ".log"):
            self._analyze_text()

        else:
            print(
                "Unrecognized or missing file extension: "
                f"'{self.extension or '(none)'}'"
            )
            print(
                "Supported types: "
                ".csv, .json, .txt, .log"
            )

    # ========================================================
    # CSV ANALYSIS
    # ========================================================

    def _analyze_csv(self):
        """
        Analyze a CSV file.

        Reports:
            Number of data rows
            Number of columns
            Column headers
            Inconsistent row lengths

        Week 5 hardening is retained through:
            PermissionError handling
            OSError handling
            CSV structure validation
        """

        try:
            with open(
                self.filepath,
                "r",
                encoding="utf-8",
                newline=""
            ) as file:

                reader = csv.reader(file)
                rows = list(reader)

        except PermissionError:
            print(
                "Cannot read this file, permission denied: "
                f"{self.filepath}"
            )
            return

        except OSError as error:
            print(f"Could not read the CSV file: {error}")
            return

        # ----------------------------------------------------
        # EMPTY CSV CHECK
        # ----------------------------------------------------

        if not rows:
            print("This CSV file is empty. No headers, no rows.")
            return

        # The first row is treated as the header.
        headers = rows[0]

        # Everything after the header is data.
        data_rows = rows[1:]

        # A tuple represents the measured shape of the file.
        # It is not intended to change after being calculated.
        file_shape = (
            len(data_rows),
            len(headers)
        )

        print("File type: CSV")
        print(f"Rows: {file_shape[0]}")
        print(f"Columns: {file_shape[1]}")
        print(f"Headers: {headers}")

        # ----------------------------------------------------
        # CSV STRUCTURE VALIDATION
        # ----------------------------------------------------

        mismatched = [
            (line_number, len(row))
            for line_number, row in enumerate(
                data_rows,
                start=2
            )
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

    # ========================================================
    # JSON ANALYSIS
    # ========================================================

    def _analyze_json(self):
        """
        Analyze the structure of a JSON file.

        Identifies whether the top-level value is:
            list
            dictionary
            single value

        Handles:
            Empty files
            Invalid JSON
            Permission errors
            Other file reading errors
        """

        try:
            with open(
                self.filepath,
                "r",
                encoding="utf-8"
            ) as file:

                raw_text = file.read()

        except PermissionError:
            print(
                "Cannot read this file, permission denied: "
                f"{self.filepath}"
            )
            return

        except OSError as error:
            print(f"Could not read the JSON file: {error}")
            return

        # ----------------------------------------------------
        # EMPTY JSON CHECK
        # ----------------------------------------------------

        if not raw_text.strip():
            print("This JSON file is empty.")
            return

        # ----------------------------------------------------
        # JSON PARSING
        # ----------------------------------------------------

        try:
            data = json.loads(raw_text)

        except json.JSONDecodeError as error:
            print(
                "This JSON file is broken and could not be read."
            )
            print(f"Reason: {error}")
            return

        # ----------------------------------------------------
        # JSON LIST
        # ----------------------------------------------------

        if isinstance(data, list):

            print("File type: JSON (list)")
            print(f"Total items: {len(data)}")

            if data:
                print(
                    "First item type: "
                    f"{type(data[0]).__name__}"
                )

                if isinstance(data[0], dict):
                    print(
                        "Keys in first item: "
                        f"{list(data[0].keys())}"
                    )

        # ----------------------------------------------------
        # JSON DICTIONARY
        # ----------------------------------------------------

        elif isinstance(data, dict):

            print("File type: JSON (dictionary)")
            print(
                f"Top-level keys: {list(data.keys())}"
            )

        # ----------------------------------------------------
        # JSON SINGLE VALUE
        # ----------------------------------------------------

        else:

            print(
                "File type: JSON "
                f"(single value: {type(data).__name__})"
            )

    # ========================================================
    # TEXT / LOG ANALYSIS
    # ========================================================

    def _analyze_text(self):
        """
        Analyze a TXT or LOG file.

        Reports:
            Total number of lines
            Number of suspicious lines
            Suspicious words found on each matching line

        Suspicious keyword matching uses SET intersection.
        """

        try:
            with open(
                self.filepath,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as file:

                lines = file.readlines()

        except PermissionError:
            print(
                "Cannot read this file, permission denied: "
                f"{self.filepath}"
            )
            return

        except OSError as error:
            print(
                f"Could not read the text/log file: {error}"
            )
            return

        # ----------------------------------------------------
        # EMPTY TEXT/LOG CHECK
        # ----------------------------------------------------

        if not lines:
            print("This text/log file is empty.")
            return

        print("File type: TEXT/LOG")
        print(f"Total lines: {len(lines)}")

        # Dictionary:
        #
        #     line number -> suspicious words
        #
        # Example:
        #
        #     {
        #         2: ["timeout"],
        #         5: ["error", "failed"]
        #     }

        findings = {}

        # ----------------------------------------------------
        # SCAN EACH LINE
        # ----------------------------------------------------

        for line_number, line in enumerate(
            lines,
            start=1
        ):

            # Convert the line into a SET of words.
            #
            # lower() makes keyword matching case-insensitive.

            words_in_line = set(
                line.lower().split()
            )

            # Set intersection returns words that appear in
            # both the current line and SUSPICIOUS_WORDS.

            matches = words_in_line & SUSPICIOUS_WORDS

            if matches:
                # sorted() makes the output predictable.
                findings[line_number] = sorted(matches)

        # ----------------------------------------------------
        # NO FINDINGS
        # ----------------------------------------------------

        if not findings:
            print("No suspicious words found.")
            return

        # ----------------------------------------------------
        # DISPLAY FINDINGS
        # ----------------------------------------------------

        print(
            f"Suspicious lines found: {len(findings)}"
        )

        for line_number, matches in findings.items():
            print(
                f"  Line {line_number}: {matches}"
            )


# ============================================================
# COMMAND LINE ENTRY POINT
# ============================================================

def main():
    """
    Start SentinelCLI from the command line.

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

    # Create an object from the FileInspector class.
    inspector = FileInspector(filepath)

    # Ask the object to analyze its own file.
    inspector.analyze()


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()