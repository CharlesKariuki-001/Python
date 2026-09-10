"""
ForgeKit — a small collection of reusable Python utilities.
This file makes the forgekit folder importable as a package, and
exposes the most commonly used functions at the top level, so users
can do `from forgekit import is_positive` instead of always writing
`from forgekit.validators import is_positive`.
"""

from .validators import is_positive, is_valid_email
from .formatters import to_title_case, format_currency
from .file_tools import count_lines, get_file_extension

__all__ = [
    "is_positive",
    "is_valid_email",
    "to_title_case",
    "format_currency",
    "count_lines",
    "get_file_extension",
]