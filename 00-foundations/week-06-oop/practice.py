"""
Week 6 Practice — Object Oriented Programming
Small, isolated exercises proving I understand classes, objects,
self, and __init__ before refactoring the real SentinelCLI.
"""

# 1. A BASIC CLASS AND OBJECT
class Transaction:
    def __init__(self, amount, recipient):
        self.amount = amount
        self.recipient = recipient

    def summary(self):
        return f"{self.recipient} received {self.amount}"

t1 = Transaction(5000, "Alice")
t2 = Transaction(200, "Bob")

print(t1.summary())
print(t2.summary())


# 2. self KEEPS EACH OBJECT'S DATA SEPARATE
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

counter_a = Counter()
counter_b = Counter()

counter_a.increment()
counter_a.increment()
counter_b.increment()

print(f"Counter A: {counter_a.count}")  # 2
print(f"Counter B: {counter_b.count}")  # 1, completely separate from A


# 3. A METHOD THAT USES self TO MAKE A DECISION
class RiskChecker:
    def __init__(self, amount):
        self.amount = amount

    def level(self):
        if self.amount > 10000:
            return "HIGH"
        elif self.amount > 1000:
            return "MEDIUM"
        return "LOW"

checker = RiskChecker(15000)
print(f"Risk level: {checker.level()}")


# 4. A CLASS THAT HOLDS STATE ACROSS MULTIPLE METHOD CALLS
class RunningTotal:
    def __init__(self):
        self.total = 0
        self.entries = []

    def add(self, value):
        self.total += value
        self.entries.append(value)

    def average(self):
        if not self.entries:
            return 0
        return self.total / len(self.entries)

tracker = RunningTotal()
tracker.add(100)
tracker.add(200)
tracker.add(300)

print(f"Total: {tracker.total}")
print(f"Average: {tracker.average()}")


# 5. A SIMPLE PREVIEW OF THE SentinelCLI REFACTOR SHAPE
class SimpleFileInspector:
    def __init__(self, filepath):
        self.filepath = filepath
        self.extension = filepath.split(".")[-1] if "." in filepath else None

    def describe(self):
        if self.extension == "csv":
            return f"{self.filepath} looks like a CSV file."
        elif self.extension == "json":
            return f"{self.filepath} looks like a JSON file."
        else:
            return f"{self.filepath} has an unrecognized type."

inspector = SimpleFileInspector("data.csv")
print(inspector.describe())