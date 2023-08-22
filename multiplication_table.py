# Write a program that prints a multiplication table for a given number.

def multiplication_table(num):
    print("Multiplication Table for", num)

    for i in range(1, 13):
        result = num * i
        print(num, "x", i, "=", result)

number = int(input("Enter a number: "))
multiplication_table(number)