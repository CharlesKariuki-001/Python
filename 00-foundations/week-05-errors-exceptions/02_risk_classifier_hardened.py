"""
Week 5 Hardened — Rule-Based Risk Classifier
Original from Week 2. This version validates input and makes the
level classification a single clean if/elif/else block.
"""


def get_transaction_amount():
    while True:
        raw_value = input("Enter transaction amount: ")
        try:
            amount = float(raw_value)
        except ValueError:
            print(f"'{raw_value}' is not a valid amount. Please enter digits only.")
            continue

        if amount < 0:
            print("A transaction amount can't be negative.")
            continue

        return amount


def get_yes_no(prompt):
    """
    Only accepts yes/no, case-insensitive, and keeps asking if the
    input is anything else. Original code treated anything that
    wasn't exactly 'yes' as a silent 'no' — including typos.
    """
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Please answer yes or no.")


def main():
    amount = get_transaction_amount()
    is_new_recipient = get_yes_no("Is this a new recipient? (yes/no): ")
    is_unusual_time = get_yes_no("Is this happening at an unusual time? (yes/no): ")

    risk_score = 0

    if amount > 10000:
        risk_score += 3
    elif amount > 1000:
        risk_score += 1

    if is_new_recipient:
        risk_score += 1

    if is_unusual_time:
        risk_score += 1

    if risk_score >= 4:
        level = "HIGH"
    elif risk_score >= 2:
        level = "MEDIUM"
    else:
        level = "LOW"

    print(f"\nRisk score: {risk_score}")
    print(f"Risk level: {level}")


if __name__ == "__main__":
    main()