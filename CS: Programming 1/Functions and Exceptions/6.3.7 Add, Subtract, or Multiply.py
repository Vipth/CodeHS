"""
This program takes two numbers, then asks the user if they want to
add, subtract, or multiply them.
"""

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))
operation = input("Choose an operation (add, subtract, multiply): ")

def add():
    print(str(num1), "+", num2, "=", str(num1 + num2))
    
def subtract():
    print(str(num1), "-", num2, "=", str(num1 - num2))
    
def multiply():
    print(str(num1), "*", num2, "=", str(num1 * num2))


if operation.lower() == "add":
    add()
elif operation.lower() == "subtract":
    subtract()
elif operation.lower() == "multiply":
    multiply()
else:
    print("Invalid operation!")
