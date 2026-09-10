"""
Week 7 Practice — Modules, Packages, and Imports
This file simulates the idea of splitting code into pieces, using
functions grouped by purpose, before building the real multi-file
ForgeKit package.
"""

# Simulating what would normally be separate files, just for practice
# in one place. The real ForgeKit build genuinely splits these apart.

# ── Simulated validators.py ─────────────────────────────────
def is_positive(number):
    return number > 0

def is_valid_email(text):
    return "@" in text and "." in text


# ── Simulated formatters.py ─────────────────────────────────
def to_title_case(text):
    return text.strip().title()

def format_currency(amount):
    return f"${amount:,.2f}"


# ── Simulated file_tools.py ─────────────────────────────────
def count_lines(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return len(f.readlines())


# ── DEMONSTRATING __name__ == "__main__" ────────────────────
def run_demo():
    print(is_positive(5))
    print(is_positive(-3))
    print(is_valid_email("someone@example.com"))
    print(is_valid_email("not an email"))
    print(to_title_case("  charles kariuki  "))
    print(format_currency(45000))


if __name__ == "__main__":
    # This block only runs when this file is executed directly,
    # e.g. `python practice.py`. If another file imported this one
    # instead, none of this would run automatically.
    run_demo()