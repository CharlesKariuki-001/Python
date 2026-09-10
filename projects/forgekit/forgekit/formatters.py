"""Formatting utilities — functions that reshape data for clean display."""


def to_title_case(text: str) -> str:
    """Converts text to Title Case, trimming extra whitespace first."""
    if not isinstance(text, str):
        raise TypeError(f"Expected a string, got {type(text).__name__}")
    return text.strip().title()


def format_currency(amount: float, symbol: str = "$") -> str:
    """Formats a number as currency with thousands separators and 2 decimal places."""
    if not isinstance(amount, (int, float)):
        raise TypeError(f"Expected a number, got {type(amount).__name__}")
    return f"{symbol}{amount:,.2f}"


def truncate(text: str, max_length: int = 50) -> str:
    """Shortens text to max_length characters, adding '...' if it was cut."""
    if len(text) <= max_length:
        return text
    return text[:max_length].rstrip() + "..."