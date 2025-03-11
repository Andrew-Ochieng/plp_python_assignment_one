def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation! Please enter +, -, *, or /.")
            return

        # Format result to remove .0 if it's a whole number
        result = int(result) if result.is_integer() else result

        print(f"{int(num1) if num1.is_integer() else num1} {operation} {int(num2) if num2.is_integer() else num2} = {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

calculator()
