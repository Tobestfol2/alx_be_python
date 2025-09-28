# arithmetic_operations.py: Defines the core arithmetic function.

def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs a basic arithmetic operation based on the 'operation' string.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The desired operation ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: The result of the operation, or an error message 
                      if division by zero or an invalid operation occurs.
    """
    
    # Use match-case for clear operation selection (requires Python 3.10+)
    match operation.lower().strip():
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                # Handle division by zero case gracefully
                return "Error: Division by zero is not allowed."
            return num1 / num2
        case _:
            # Handle invalid operation input
            return f"Error: Invalid operation '{operation}'. Please choose add, subtract, multiply, or divide."
