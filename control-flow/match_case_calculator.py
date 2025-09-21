# This script is a simple calculator that uses a match-case statement.

# Get user input for two numbers
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    # Exit the script if input is not a number
    exit()

# Get user input for the operation
operation = input("Choose the operation (+, -, *, /): ")

# Use a match-case statement to perform the calculation
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        result = num1 - num2
        print(f"The result is {result}")
    case '*':
        result = num1 * num2
        print(f"The result is {result}")
    case '/':
        # Handle division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation. Please choose from +, -, *, or /.")
        