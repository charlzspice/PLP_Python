def calculator():
    print("Welcome to the Basic Calculator!")
    print("Available operations: +, -, *, /")
    
    try:
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        
        # Perform calculation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
                return
            result = num1 / num2
        else:
            print("Invalid operation! Please use +, -, *, or /")
            return
        
        # Display result
        print(f"\nResult: {num1} {operation} {num2} = {result}")
    
    except ValueError:
        print("Error: Please enter valid numbers!")

# Run the calculator
calculator()