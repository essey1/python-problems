# Create a program that generates a random number, and the user has to guess it

import random

def guess_number():
    target_number = random.randint(1, 10)
    attempts = 0

    while True:
        user_guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1

        if user_guess == target_number:
            print("Congratulations! You guessed the number correctly.")
            print("Number of attempts:", attempts)
            break
        elif user_guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Run the game
print("Welcome to the Number Guessing Game!")
guess_number()