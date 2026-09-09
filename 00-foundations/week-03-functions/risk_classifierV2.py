#Risk_ClassifierV2

def get_amount_score(amount):
    if amount > 10000:
        return 3
    elif amount > 1000:
        return 1
    return 0

def get_flag_score(is_new_recipient, is_unusual_time):
    score = 0
    if is_new_recipient:
        score +=1
    if is_unusual_time:
        score +=1
    return score

def get_risk_level(score):
    if score >= 4:
        return "HIGH"
    elif score >= 2:
        return "MEDIUM"
    return "LOW"

def main():
    amount = float(input("Enter transaction amount: "))
    is_new_recipient = input("Is this a new recipient? (yes/no): ").lower() == "yes"
    is_unusual_time = input("Is this happening ata an unusual time? (yes/no)").lower() == "yes"
    
    total_score = get_amount_score(amount) + get_flag_score(is_new_recipient, is_unusual_time)
    level = get_risk_level(total_score)
     
    print(f"\nRisk score: {total_score}")
    print(f"\nRisk level: {level}")
           
main()         