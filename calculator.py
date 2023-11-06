def add(x, y):  # addition
    return x + y

def subtract(x, y): # subtraction
    return x - y

def multiply(x, y): # multiplication
    return x * y

def divide(x, y):  # division
    if y == 0:
        return "Cannot divide by zero"
    return x / y

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)
else:
    result = "Invalid operation"

print(f"Result: {result}")
