#Rule-Based Risk Classifier
#This tool looks at a transaction amount and a couple of flags, and decides how risky it looks

amount = float(input("Enter tranaction amount: "))
is_new_recipient = input("Is this a new recipient? (yes/no): ").lower() == "yes"
is_unusual_time = input("Is this happening at an unusual time? (yes/no): ").lower()=="yes"

risk_score = 0

if amount > 10000:
    risk_score += 3
elif amount > 1000:
    risk_score += 1
    
if is_new_recipient:
    risk_score +=1    
    
if is_unusual_time:
    risk_score += 1
    
if risk_score >= 4:
    level = "HIGH"
elif risk_score >=2:
    level = "MEDIUM"
    
else:
    level = "LOW"
    
print(f"\nRisk score: {risk_score}")
print(f"Risk level: {level}")                    
       