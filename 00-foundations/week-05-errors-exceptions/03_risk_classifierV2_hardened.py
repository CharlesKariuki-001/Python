"""
Week 5 Hardened — Risk Classifier V2
Original from Week 3. Same validation approach as V1, but applied
across the function-based structure this version introduced.
"""


def get_amount_score(amount):
    if amount > 10000:
        return 3
    elif amount > 1000:
        return 1
    return 0


def get_flag_score(is_new_recipient, is_unusual_time):
    score = 0
    if is_new_recipient:
        score += 1
    if is_unusual_time:
        score += 1
    return score


def get_risk_level(score):
    if score >= 4:
        return "HIGH"
    elif score >= 2:
        return "MEDIUM"
    return "LOW"


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

    total_score = get_amount_score(amount) + get_flag_score(is_new_recipient, is_unusual_time)
    level = get_risk_level(total_score)

    print(f"\nRisk score: {total_score}")
    print(f"Risk level: {level}")


if __name__ == "__main__":
    main()