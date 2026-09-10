"""
ForgeKit Demo — proves the package works correctly when imported
from outside the forgekit folder, the way a real user would use it.
"""

from forgekit import (
    is_positive,
    is_valid_email,
    to_title_case,
    format_currency,
    count_lines,
    get_file_extension,
)


def main():
    print("--- Validators ---")
    print(f"is_positive(5): {is_positive(5)}")
    print(f"is_positive(-3): {is_positive(-3)}")
    print(f"is_valid_email('someone@example.com'): {is_valid_email('someone@example.com')}")
    print(f"is_valid_email('not an email'): {is_valid_email('not an email')}")

    print("\n--- Formatters ---")
    print(f"to_title_case('  charles kariuki  '): '{to_title_case('  charles kariuki  ')}'")
    print(f"format_currency(45000): {format_currency(45000)}")

    print("\n--- File Tools ---")
    print(f"get_file_extension('demo.py'): {get_file_extension('demo.py')}")
    print(f"count_lines('demo.py'): {count_lines('demo.py')} lines")


if __name__ == "__main__":
    main()