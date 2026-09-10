"""
Tests for ForgeKit. Run with: pytest
These import forgekit the same way a real user would, confirming
the package is genuinely usable from outside itself.
"""

import pytest
from forgekit import (
    is_positive,
    is_valid_email,
    to_title_case,
    format_currency,
    get_file_extension,
)


def test_is_positive():
    assert is_positive(5) is True
    assert is_positive(-3) is False
    assert is_positive(0) is False


def test_is_valid_email():
    assert is_valid_email("someone@example.com") is True
    assert is_valid_email("not an email") is False
    assert is_valid_email(12345) is False  # wrong type, should not crash


def test_to_title_case():
    assert to_title_case("  charles kariuki  ") == "Charles Kariuki"


def test_to_title_case_wrong_type():
    with pytest.raises(TypeError):
        to_title_case(12345)


def test_format_currency():
    assert format_currency(45000) == "$45,000.00"
    assert format_currency(45000, symbol="Ksh ") == "Ksh 45,000.00"


def test_get_file_extension():
    assert get_file_extension("data.csv") == ".csv"
    assert get_file_extension("no_extension_file") is None