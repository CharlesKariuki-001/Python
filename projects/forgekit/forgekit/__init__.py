"""
ForgeKit — a small collection of reusable Python utilities.

This file makes the forgekit folder importable as a package and
exposes commonly used functions at the top level.
"""

from .validators import is_positive, is_valid_email, is_non_empty_string
from .formatters import to_title_case, format_currency, truncate
from .file_tools import count_lines, get_file_extension

__all__ = [
    "is_positive",
    "is_valid_email",
    "is_non_empty_string",
    "to_title_case",
    "format_currency",
    "truncate",
    "count_lines",
    "get_file_extension",
]