"""
calculator.py

A professional command-line calculator in Python that performs
basic arithmetic operations: addition, subtraction, multiplication,
and division. Prompts user for input and handles errors gracefully.
"""

def add(x: float, y: float) -> float:
    """Return the sum of x and y."""
    return x + y

def subtract(x: float, y: float) -> float:
    """Return the difference of x and y."""
    return x - y

def multiply(x: float, y: float) -> float:
    """Return the product of x and y."""
    return x * y

def divide(x: float, y: float) -> float | str:
    """Return the quotient of x and y, or an error if division by zero."""
    if y == 0:
        return "❌ Error: Cannot divide by zero."
    return x / y

def get_number(prompt: str) -> float:
    """Prompt the user to enter a number and validate the input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️ Invalid input. Please enter a numeric value.")

def get_operation_choice() -> str:
    """Display a menu and get the user's operation choice."""
    print("\nChoose an operation:")
    print("1. Addition       (+)")
    print("2. Subtraction    (-)")
    print("3. Multiplication (*)")
    print("4. Division       (/)")
    return input("Enter choice (1/2/3/4): ").strip()

def perform_calculation(choice: str, num1: float, num2: float):
    """Perform the selected arithmetic operation."""
    match choice:
        case '1':
            return num1, '+', num2, add(num1, num2)
        case '2':
            return num1, '-', num2, subtract(num1, num2)
        case '3':
            return num1, '*', num2, multiply(num1, num2)
        case '4':
            return num1, '/', num2, divide(num1, num2)
        case _:
            return None

def main():
    """Main function to run the calculator."""
    print("🔢 [ Simple Arithmetic Calculator ]")

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    choice = get_operation_choice()

    result = perform_calculation(choice, num1, num2)

    if result is None:
        print("❌ Invalid operation selected.")
    else:
        a, op, b, res = result
        print(f"\n✅ Result: {a} {op} {b} = {res}")

if __name__ == "__main__":
    main()
