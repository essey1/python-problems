# Write a function to calculate the factorial of a number using recursion.

def factorial(n):
    if n == 0:  # Factorial of 0 is 1
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
number = int(input("Enter a number: "))
result = factorial(number)
print("Factorial:", result)