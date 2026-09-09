#How python holds real-world data eg CSV, JSON, API response, long file, database row



#lists (an ordered collectionof things)
amounts = [500,1200, 300, 50000]
print(amounts[0])
print(amounts[-1])

amounts.append(700)
amounts.remove(300)
for amount in amounts:
    print(amount)
    
 
    
#Dictionaries - labeled data
#when you want to look things up by name

transaction = {
    "amount": 5000,
    "recipient": "new_user_882",
    "flagged": True
}
print(transaction["amount"])
print(transaction.get("currency"))
   
   
   
#tuples(locked list)
coordinates = (35.6895, 139.6917)



#sets(collection with no duplicates, and no order)- they are perect for removing duplicates automatically and checking "is this thing here?" extremely fast. 
suspicious_words = {"error", "failed", "unauthorized"}
 #suport real set math
a = {"error", "failed", "denied"}
b = {"failed", "timeout"}

print(a & b)   
print(a | b)   
print(a - b)      



#Comprehessions(builds a collection in one line)
amount = [500, 1200, 300]
  #long way
doubled = []
for a in amounts:
    doubled.append(a * 2)
   # Comprehension way (same result)
doubled = [a * 2 for a in amounts if a > 400]
 
 
 
 #Nested data(collections inside collections)
 
data = {
    "user": "charles",
    "transactions": [
        {"amount": 500, "flagged": False},
        {"amount": 12000, "flagged": True}
    ]
}

print(data["transactions"][1]["amount"])   # 12000