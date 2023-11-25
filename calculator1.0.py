# functions
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

# user
print ("calculator 1.0")
x = float(input("Number 1: "))
op = (input("Action: "))
y = float(input("Number 2: "))

# calculate
if op == ("+"):
    print (add(x, y))
if op == ("-"):
    print (subtract(x, y))
if op == ("*"):
    print (multiply(x, y))
if op == ("/"):
    print (divide(x, y))