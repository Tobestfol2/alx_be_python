# This script draws a square pattern of asterisks based on user input,
# using a while loop nested with a for loop.

# Prompt the user for the size of the pattern
try:
    size = int(input("Enter the size of the pattern: "))
    # Ensure the size is a positive integer
    if size <= 0:
        print("Please enter a positive integer.")
    else:
        # Use a while loop to iterate through each row
        row = 0
        while row < size:
            # Use a for loop to print asterisks for each column in the current row
            for col in range(size):
                print("*", end="")
            
            # Print a newline character after each row is complete
            print()
            
            # Increment the row counter
            row += 1

except ValueError:
    print("Invalid input. Please enter a valid integer.")
