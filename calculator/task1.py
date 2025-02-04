#making calculator

# Function to perform calculations
def calculator():
    # Get user input for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Display the available operations
    print("\nSelect the operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    # Get user input for the operation
    operation = input("Enter the number corresponding to the operation: ")

    # Perform the calculation based on the chosen operation
    if operation == "1":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    elif operation == "2":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    elif operation == "3":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    elif operation == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print("Error: Division with zero is not possible.")
    else:
        print("Invalid operation choice.")

#calling function.
calculator()
