# Create a program that counts the number of vowels in a given string.

def count_vowels(string):
    vowel_count = 0
    string = string.lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # Count the number of vowels in the string
    for char in string:
        if char in vowels:
            vowel_count += 1

    print("Number of vowel(s):", vowel_count)

# Prompt the user and execute the function
string = input("Enter a string: ")
count_vowels(string)
