# Create a function that determines whether a given string is a pangram (contains all the letters of the alphabet).

import string

def pangram_checker(text):
    letters = set()

    # Makes the program case insenstive
    text = text.lower()

    for char in text:
        if char.isalpha():
            letters.add(char)

    if letters == set(string.ascii_lowercase):
        print("This text is a pangram.")
    else:
        print("This text is not a pangram.")

pangram_checker(input("Enter a text:"))
        