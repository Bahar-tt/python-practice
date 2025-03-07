def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y
try:
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    result = divide(num1, num2)
    print("Result:", result)
except ZeroDivisionError as e:
    print("Error:", e)
except ValueError:
    print("Invalid input! Please enter numeric values.")
    