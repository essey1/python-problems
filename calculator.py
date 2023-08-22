# Create a calculator program that performs basic arithmetic operations (+, -, *, /,%,**) and takes instructions from the user.

def calculator():
    print("Welcome! I'm a calculator.\nAnd these are the arithmetic operations I can do.")
    print("Enter 'add' to perform addition.")
    print("Enter 'subtract' to perform subtraction.")
    print("Enter 'multiply' to perform multiplication.")
    print("Enter 'divide' to perform division.")
    print("Enter 'remaineder' to calculate the remainder.")
    print("Enter 'power' to calculate exponentiation.")
    print("Enter 'quit' to exit the program.")

    while True:
        instruction = input("Enter an arithmetic operation: ")

        if instruction == "add":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 + num2
            print("Result:", result)
        elif instruction == "subtract":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 - num2
            print("Result:", result)
        elif instruction == "multiply":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 * num2
            print("Result:", result)
        elif instruction == "divide":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 / num2
            print("Result:", result)
        elif instruction == "remainder":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 % num2
            print("Result:", result)
        elif instruction == "power":
            num1 = float(input("Enter the base number: "))
            num2 = float(input("Enter the exponent: "))
            result = num1 ** num2
            print("Result:", result)
        elif instruction == "quit":
            print("Exiting the calculator program.")
            break
        else:
            print("Invalid operation. Please try again.")

calculator()