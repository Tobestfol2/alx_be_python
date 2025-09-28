# temp_conversion_tool.py: Demonstrates using global variables for conversion factors.

# --- Global Conversion Factors ---
# Factors are defined once globally and can be accessed (read) by functions.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.
    Formula: Celsius = (Fahrenheit - 32) * (5/9)
    """
    # Accessing the global variable FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.
    Formula: Fahrenheit = (Celsius * 9/5) + 32
    """
    # Accessing the global variable CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Handles user interaction, input validation, and displays the conversion results.
    """
    print("--- Temperature Conversion Tool ---")
    
    # Input for temperature value
    while True:
        temp_input = input("Enter the temperature value: ").strip()
        try:
            temperature = float(temp_input)
            break
        except ValueError:
            # Raise the specified error if input is not a number
            raise ValueError("Invalid temperature. Please enter a numeric value.")
            
    # Input for unit
    unit = input("Is this temperature in Celsius (C) or Fahrenheit (F)? ").strip().upper()
    
    # Perform conversion based on input unit
    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"\n{temperature}°F is equal to {converted_temp:.2f}°C")
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"\n{temperature}°C is equal to {converted_temp:.2f}°F")
    else:
        print("Invalid unit specified. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
