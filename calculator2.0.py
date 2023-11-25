# Functions
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

# User
print ("calculator 2.0")
x, op, y = input("Calculate 2 numbers: "). split(" ")
num1 = float(x)
num2 = float(y)

# Calculate
if op == ("+"):
    print (add(num1, num2))
if op == ("-"):
    print (subtract(num1, num2))
if op == ("*"):
    print (multiply(num1, num2))
if op == ("/"):
    print (divide(num1, num2))