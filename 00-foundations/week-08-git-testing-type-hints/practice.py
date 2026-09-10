"""
Week 8 Practice — Type Hints and Proper Testing
Small exercises proving I understand type hints and how to write
tests that cover normal, edge, and failure cases, not just one
happy-path check per function.
"""

from typing import Optional, List


# ── TYPE HINTS ───────────────────────────────────────────────
def add(a: float, b: float) -> float:
    return a + b


def get_first_name(full_name: str) -> str:
    return full_name.strip().split(" ")[0]


def find_by_id(records: List[dict], target_id: int) -> Optional[dict]:
    """
    Optional[dict] tells anyone reading this: this function might
    return a dict, or it might return None if nothing matched.
    """
    for record in records:
        if record.get("id") == target_id:
            return record
    return None


# ── DEMONSTRATING THE THREE KINDS OF TEST CASES ─────────────
# These aren't real pytest tests here, just a plain demonstration
# of the thinking, before writing real tests in the actual files.

def demonstrate_test_thinking():
    # Normal case
    assert add(2, 3) == 5

    # Edge case — zero
    assert add(0, 0) == 0

    # Edge case — negative numbers
    assert add(-5, 5) == 0

    print("All manual checks passed.")


# ── A SMALL EXAMPLE OF pytest.raises IN ACTION ──────────────
def strict_divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    demonstrate_test_thinking()

    print(find_by_id([{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}], 2))
    print(find_by_id([{"id": 1, "name": "Alice"}], 99))  # None, not found

    try:
        strict_divide(10, 0)
    except ValueError as e:
        print(f"Caught expected error: {e}")