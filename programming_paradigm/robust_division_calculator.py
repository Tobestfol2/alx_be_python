# robust_division_calculator.py: Contains the safe division function with error handling.

def safe_divide(numerator, denominator):
    """
    Performs division safely, handling ZeroDivisionError and ValueError.

    :param numerator: The string or number representing the numerator.
    :param denominator: The string or number representing the denominator.
    :return: The result (float) or an appropriate error message (string).
    """
    try:
        # Step 1: Attempt to convert input strings to floating-point numbers.
        num1 = float(numerator)
        num2 = float(denominator)

    except ValueError:
        # Catches cases where input cannot be converted to a float (e.g., 'ten' or 'abc').
        return "Error: Please enter numeric values only."

    try:
        # Step 2: Perform the division.
        result = num1 / num2
        
        # Return the result for successful division.
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Catches the specific error when the denominator is 0.
        return "Error: Cannot divide by zero."
