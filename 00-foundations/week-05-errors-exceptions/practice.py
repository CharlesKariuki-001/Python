"""
Week 5 Practice — Errors, Exceptions, and Debugging
Small, isolated exercises proving I understand exception handling
before applying it to harden the real Week 1 to 4 builds.
"""

# 1. CATCHING A SPECIFIC EXCEPTION, NOT A BARE EXCEPT
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))


# 2. try / except / else / finally, ALL TOGETHER
def read_first_line(filepath):
    try:
        f = open(filepath, "r")
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    else:
        first_line = f.readline()
        print("File opened successfully.")
        return first_line
    finally:
        print("Finished attempting to read the file.")

read_first_line("does_not_exist.txt")


# 3. CATCHING MULTIPLE DIFFERENT EXCEPTION TYPES
def safe_int_convert(value):
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' is not a valid number.")
        return None
    except TypeError:
        print(f"Cannot convert {type(value).__name__} to a number.")
        return None

print(safe_int_convert("42"))
print(safe_int_convert("not a number"))
print(safe_int_convert(None))


# 4. SAFE DICTIONARY ACCESS, THE .get() LESSON FROM WEEK 4, APPLIED HERE
def get_user_status(record):
    # Unsafe version would be record["status"], which crashes if missing
    status = record.get("status", "unknown")
    return status

print(get_user_status({"user": "alice", "status": "active"}))
print(get_user_status({"user": "bob"}))  # no status key at all


# 5. RAISING MY OWN EXCEPTION WITH A CLEAR MESSAGE
def load_config(data):
    if "api_key" not in data:
        raise ValueError("Config is missing the required 'api_key' field.")
    return data

try:
    load_config({"timeout": 30})
except ValueError as e:
    print(f"Config error: {e}")


# 6. THE DEBUGGING PROCESS, DEMONSTRATED ON A SMALL BROKEN EXAMPLE
def calculate_average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

# Reproduce a failure on purpose
try:
    calculate_average([])
except ZeroDivisionError:
    print("Cannot calculate an average of an empty list.")

# The actual fix, applied
def calculate_average_safe(numbers):
    if not numbers:
        raise ValueError("Cannot calculate an average of an empty list.")
    return sum(numbers) / len(numbers)

try:
    calculate_average_safe([])
except ValueError as e:
    print(f"Handled cleanly: {e}")