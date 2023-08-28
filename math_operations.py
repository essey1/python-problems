# Write a program that takes two numbers as input and prints their sum, difference, product, and quotient.

def calculate_operations(num1, num2):
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2

    print("Sum: ", sum)
    print("Difference: ", difference)
    print("Product: ", product)
    print("Quotient: ", quotient)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

calculate_operations(num1, num2)