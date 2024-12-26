def calculator():
    print("Welcome to the Simple Calculator!")

    try:
        # Prompt user for input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("Choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Enter your choice (1/2/3/4): ")

        # Perform calculation based on user's choice
        if operation == "1":
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operation == "2":
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operation == "3":
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operation == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation choice. Please try again.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
