# ForgeKit

A small, reusable Python package of everyday utilities — validators, formatters, and file tools — built to practice modules, packages, and clean imports.

This is the Week 7 flagship project of the Python Forge 180-day build, built after learning how Python organizes code across multiple files instead of one.

## The Problem

A single-file script is fine for a small tool, but real projects grow. Once you have more than a handful of related functions, keeping everything in one file makes it harder to find what you need and harder to reuse pieces elsewhere. ForgeKit demonstrates the fix: splitting related functions into focused modules, grouped into one importable package.

## Structure
forgekit/
├── forgekit/
│ ├── init.py # exposes the package's public functions
│ ├── validators.py # is_positive, is_valid_email, is_non_empty_string
│ ├── formatters.py # to_title_case, format_currency, truncate
│ └── file_tools.py # count_lines, get_file_extension, file_size_kb
├── demo.py # proves the package works from the outside
├── tests/
│ └── test_forgekit.py
├── conftest.py # tells pytest where the project root is
├── requirements.txt
└── README.md


## Install

```bash
git clone https://github.com/CharlesKariuki-001/Python.git
cd Python/projects/forgekit
python -m venv .venv
.venv\Scripts\activate      # Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```python
from forgekit import is_positive, format_currency, count_lines

is_positive(5)                  # True
format_currency(45000)          # '$45,000.00'
count_lines("some_file.txt")    # number of lines in the file
```

Or run the included demo directly:

```bash
python demo.py
```

--- Validators ---
is_positive(5): True
is_positive(-3): False
is_valid_email('someone@example.com'): True
is_valid_email('not an email'): False

--- Formatters ---
to_title_case(' charles kariuki '): 'Charles Kariuki'
format_currency(45000): $45,000.00

--- File Tools ---
get_file_extension('demo.py'): .py
count_lines('demo.py'): 33 lines


## Testing

```bash
pytest
```

All 6 tests cover the validators, formatters, and file tools, including type-checking edge cases (e.g. passing a number where a string was expected).

## What I Learned Building This

The real lesson here wasn't the individual functions, it was the shape of a multi-file project: an `__init__.py` that exposes a clean public interface, modules organized by purpose rather than by when I happened to write them, and a `demo.py` that imports the package the same way an actual user would, rather than testing from inside the package itself.

I also learned that pytest needs an explicit signal, an empty `conftest.py` at the project root, to know where to search for the package being tested. Without it, the tests fail with a `ModuleNotFoundError` even though the code itself is completely correct. This is a good example of a "looks like a code bug but is actually a project-structure and tooling issue" — a distinction that matters a lot for real debugging work.

## Limitations

The email validator is intentionally simple; it checks for a basic shape (`@` and a `.` after it), not real email deliverability. These utilities are general-purpose building blocks, not a finished product, most are reused inside later, larger projects rather than sold as a standalone tool.

## Need Reusable Utilities Like This for Your Project?

If you're building something in Python and want clean, tested, reusable building blocks instead of one long tangled script, get in touch.

📬 [LinkedIn](https://ke.linkedin.com/in/charles-mburu-838965382) · [X](https://x.com/KariukiBuilds__)