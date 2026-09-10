"""File utilities — small, reusable helpers for working with files."""

import os


def count_lines(filepath):
    """Returns the number of lines in a text file. Raises FileNotFoundError if missing."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No such file: {filepath}")
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        return len(f.readlines())


def get_file_extension(filepath):
    """Returns the file extension in lowercase, or None if there isn't one."""
    _, extension = os.path.splitext(filepath)
    return extension.lower() if extension else None


def file_size_kb(filepath):
    """Returns file size in kilobytes, rounded to 2 decimal places."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No such file: {filepath}")
    size_bytes = os.path.getsize(filepath)
    return round(size_bytes / 1024, 2)