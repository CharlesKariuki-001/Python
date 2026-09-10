"""
Week 4 Practice — Collections
Small, isolated exercises. Nothing here is the real SentinelCLI build —
this is just proving I understand each concept before using it for real.
"""

# ── 1. LISTS ────────────────────────────────────────────────
suspicious_words_list = ["error", "failed", "unauthorized", "error"]
print("First word:", suspicious_words_list[0])
print("Total words (with duplicates):", len(suspicious_words_list))

# ── 2. DICTIONARIES ─────────────────────────────────────────
file_summary = {"rows": 120, "columns": 5, "filename": "data.csv"}

# Unsafe way — crashes if key is missing
print("Rows:", file_summary["rows"])

# Safe way — never crashes
print("Missing key with .get():", file_summary.get("author"))
print("Missing key with default:", file_summary.get("author", "unknown"))

# ── 3. TUPLES ────────────────────────────────────────────────
file_shape = (120, 5)  # (rows, columns) — should never change
print("File shape:", file_shape)

try:
    file_shape[0] = 999  # this should fail — tuples are locked
except TypeError as e:
    print("Tuples can't be changed — confirmed:", e)

# ── 4. SETS ──────────────────────────────────────────────────
suspicious_words = {"error", "failed", "unauthorized", "attack"}
found_words = {"login", "error", "success"}

print("Overlap (&):", suspicious_words & found_words)
print("Combined (|):", suspicious_words | found_words)
print("Only in suspicious (-):", suspicious_words - found_words)

# Fast membership check — this is the SentinelCLI trick
word_to_check = "unauthorized"
print(f"Is '{word_to_check}' suspicious?", word_to_check in suspicious_words)

# ── 5. COMPREHENSIONS ───────────────────────────────────────
# Long way
squares_long = []
for n in range(5):
    squares_long.append(n * n)

# Short way — same result
squares_short = [n * n for n in range(5)]

print("Long way:", squares_long)
print("Short way:", squares_short)

# A more realistic comprehension: pull out only the flagged lines
lines = ["login ok", "error: timeout", "user created", "failed: bad password"]
flagged = [line for line in lines if "error" in line or "failed" in line]
print("Flagged lines:", flagged)

# ── 6. NESTED DATA ───────────────────────────────────────────
file_report = {
    "filename": "log.txt",
    "issues": [
        {"line": 12, "word": "unauthorized"},
        {"line": 45, "word": "failed"},
    ],
}

print("First issue's word:", file_report["issues"][0]["word"])

# Loop through nested data — this is exactly the shape real data has
for issue in file_report["issues"]:
    print(f"Line {issue['line']}: found '{issue['word']}'")