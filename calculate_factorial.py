# Write a function to calculate the factorial of a number using recursion.

def factorial(num):
    if num == 0:  # Factorial of 0 is 1
        return 1
    else:
        return num * factorial(num - 1)

number = int(input("Enter a number: "))
result = factorial(number)
print("Factorial:", result)