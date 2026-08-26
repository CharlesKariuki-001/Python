income = float(input("Enter your income: "))
expenses = float(input("Enter you expenses: "))

savings = income - expenses
savings_rate = (savings / income) *100 if income > 0 else 0

print(f"\n--- Your Stats ---")
print(f"Income: {income}")
print(f"Expenses:{expenses}")
print(f"Savings: {savings}")
print(f"Savings rate: {savings_rate:.1f}%")
print(f"Are you saving money? {savings > 0}")