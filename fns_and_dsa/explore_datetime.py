# explore_datetime.py: Demonstrates usage of the datetime and timedelta objects.
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains and displays the current date and time in a specified format.
    """
    # Part 1: Display the Current Date and Time
    
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the date and time string
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the result
    print("\n--- Current Date and Time ---")
    print(f"Current Date and Time: {formatted_date}")
    print("-----------------------------")

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates the future date.
    """
    # Part 2: Calculate a Future Date
    
    # Get the current date (we only need the date part for this calculation)
    today = datetime.now().date()
    
    # Input loop to ensure a valid integer is entered
    while True:
        try:
            days_to_add = int(input("Enter the number of days to add: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Create a timedelta object with the specified number of days
    time_difference = timedelta(days=days_to_add)
    
    # Calculate the future date by adding the timedelta to today's date
    future_date = today + time_difference
    
    # Format the future date as YYYY-MM-DD
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    # Print the result
    print(f"\nIf today is {today.strftime('%Y-%m-%d')}, then {days_to_add} days from now will be:")
    print(f"Future Date: {formatted_future_date}")


# Main execution block
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
