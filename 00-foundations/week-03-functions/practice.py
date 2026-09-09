#A function is a mini-program with a name. You define it once, then call it as many times as you want.

def greet():
    print("Hello!")
    
greet()
greet()

#parameters
def greet(name):
    print (f"Hello, {name}!")
    
greet("Faith")
greet("Charles")
    
#Return values — getting an answer back
def add(a, b):
    return a + b

result = add(3, 4)
print(result) 
    
#Default arguments — making parameters optional
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
    
greet("Faith")
greet("Faith", "Good morning")        

#Scope — where a variable "lives"
def calculate():
    x = 10
    return x

calculate()
print(x)
