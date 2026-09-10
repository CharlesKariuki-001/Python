"""Validation utilities — functions that check whether something meets a rule."""


def is_positive(number):
    """Returns True if number is greater than zero."""
    return number > 0


def is_valid_email(text):
    """
    A simple, intentionally basic email check. Real email validation
    is more complex than this; this is good enough for a quick sanity
    check, not for verifying an email actually exists.
    """
    if not isinstance(text, str):
        return False
    return "@" in text and "." in text.split("@")[-1]


def is_non_empty_string(value):
    """Returns True if value is a string with actual content, not just whitespace."""
    return isinstance(value, str) and value.strip() != ""