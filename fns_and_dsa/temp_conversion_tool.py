# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Get temperature input
        temperature = input("Enter the temperature value: ")
        # Validate temperature is numeric
        temperature = float(temperature)
        
        # Get unit input
        unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()
        
        # Perform conversion based on unit
        if unit == 'C':
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {result:.2f}°F")
        elif unit == 'F':
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {result:.2f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
            
    except ValueError as e:
        if str(e).startswith("Invalid unit"):
            print(str(e))
        else:
            print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()