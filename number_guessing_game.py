# Number Guessing Game - Marshall Ferguson - 6/2020

# Imports

import random

# TODO - Generate a random number between 1 and a user-defined upper limit

print("Welcome to the Number Guessing Game!")
upper_limit = input("Please enter an upper limit for the range of potential numbers:     ")
upper_limit = int(upper_limit)
random_number = random.randint(1, upper_limit)

# TODO - Prompt the user to guess the random number
    # TODO - Let the user know if the number they guessed was higher or lower than generated number
    # TODO - Increment the user's guess count if the user guesses incorrectly
    # TODO - Print out the generated number and guess count when user guesses correctly

guess = 0
guess_count = 0
while guess != random_number:
    guess = input("Guess what the number is!     ")
    guess = int(guess)
    if guess > random_number:
        print("Uh Oh! Your guess was over the number.....")
        guess_count = guess_count + 1
    elif guess < random_number:
        print("Uh Oh! Your guess was under the number.....")
        guess_count = guess_count + 1
    elif guess == random_number:
        print("Yay! You guessed the number!")
        guess_count = guess_count + 1
        print("It took you {} guesses!".format(guess_count))