"""
Week 5 Hardened — Income/Expense Analyzer
Original from Week 1. This version adds input validation so bad
input gets a clear message instead of a raw crash.
"""


def get_positive_number(prompt):
    """
    Keeps asking until the user gives a valid, non-negative number.
    This is the core Week 5 lesson applied: don't trust input blindly,
    catch the specific exception you expect, and give a clear message.
    """
    while True:
        raw_value = input(prompt)
        try:
            value = float(raw_value)
        except ValueError:
            print(f"'{raw_value}' is not a valid number. Please enter digits only, like 25000.")
            continue

        if value < 0:
            print("That can't be negative. Please enter a positive number.")
            continue

        return value


def main():
    income = get_positive_number("Enter your income: ")
    expenses = get_positive_number("Enter your expenses: ")

    savings = income - expenses
    savings_rate = (savings / income) * 100 if income > 0 else 0

    print(f"\n--- Your Stats ---")
    print(f"Income: {income}")
    print(f"Expenses: {expenses}")
    print(f"Savings: {savings}")
    print(f"Savings rate: {savings_rate:.1f}%")
    print(f"Are you saving money? {savings > 0}")


if __name__ == "__main__":
    main()