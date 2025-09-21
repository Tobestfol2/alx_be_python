# This script generates a multiplication table for a given number using a for loop.

# Prompt the user for a number and convert the input to an integer
try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# Use a for loop to iterate from 1 to 10
for i in range(1, 11):
    # Calculate the product
    product = number * i
    # Print the result in the specified format
    print(f"{number} * {i} = {product}")
5