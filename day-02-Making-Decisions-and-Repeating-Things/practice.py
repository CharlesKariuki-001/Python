#if/elif/else
amount = 100000

if amount > 1000:
    print("HIGH")
elif amount > 300:
    print("MEDIUM")
else:
    print ("LOW")
    
#Comparisons ==  !=  >  <  >=  <=

#Logical operators — combining questions
is_flagged = True
amount = 200

if amount > 100 and is_flagged:
    print("Needs review")    
    
# for loops — repeating over a known set
transactions = [50, 1200, 300, 5000]
for t in transactions:
    print(t)
    
# range() — repeating a number of times
for i in range(5):
      print(i)
        
# while loops — repeating until something changes 
attempts = 0

while attempts < 3:
    print("Trying...")
    attempts = attempts + 1       