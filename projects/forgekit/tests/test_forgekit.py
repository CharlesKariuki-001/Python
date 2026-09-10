"""
Tests for ForgeKit. Run with: pytest
Each function is tested against a normal case, an edge case, and a
failure case, rather than just one happy-path check.
"""

import pytest

from forgekit import (
    is_positive,
    is_valid_email,
    is_non_empty_string,
    to_title_case,
    format_currency,
    truncate,
    get_file_extension,
    count_lines,
)


# ── validators.py ────────────────────────────────────────────

def test_is_positive_normal_case():
    assert is_positive(5) is True


def test_is_positive_edge_case_zero():
    assert is_positive(0) is False


def test_is_positive_failure_case_negative():
    assert is_positive(-3) is False


def test_is_valid_email_normal_case():
    assert is_valid_email("someone@example.com") is True


def test_is_valid_email_edge_case_no_dot():
    assert is_valid_email("someone@example") is False


def test_is_valid_email_failure_case_wrong_type():
    assert is_valid_email(12345) is False


def test_is_non_empty_string_normal_case():
    assert is_non_empty_string("hello") is True


def test_is_non_empty_string_edge_case_whitespace_only():
    assert is_non_empty_string("   ") is False


# ── formatters.py ────────────────────────────────────────────

def test_to_title_case_normal_case():
    assert to_title_case("  charles kariuki  ") == "Charles Kariuki"


def test_to_title_case_edge_case_empty_string():
    assert to_title_case("") == ""


def test_to_title_case_failure_case_wrong_type():
    with pytest.raises(TypeError):
        to_title_case(12345)


def test_format_currency_normal_case():
    assert format_currency(45000) == "$45,000.00"


def test_format_currency_edge_case_zero():
    assert format_currency(0) == "$0.00"


def test_format_currency_custom_symbol():
    assert format_currency(1000, symbol="Ksh ") == "Ksh 1,000.00"


def test_format_currency_failure_case_wrong_type():
    with pytest.raises(TypeError):
        format_currency("not a number")


def test_truncate_normal_case():
    assert truncate("hello world", max_length=5) == "hello..."


def test_truncate_edge_case_exact_length():
    assert truncate("hello", max_length=5) == "hello"


# ── file_tools.py ────────────────────────────────────────────

def test_get_file_extension_normal_case():
    assert get_file_extension("data.csv") == ".csv"


def test_get_file_extension_edge_case_no_extension():
    assert get_file_extension("no_extension_file") is None


def test_count_lines_failure_case_missing_file():
    with pytest.raises(FileNotFoundError):
        count_lines("this_file_does_not_exist.txt")