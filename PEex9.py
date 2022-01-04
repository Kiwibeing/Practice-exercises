# Guessing Game One: Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 

import random

actual = random.randint(1, 9)
guess = 0
while guess != actual and guess != 'exit':
    guess = input('Guess a number between 1 to 9, inclusive: ')
    if guess == 'exit':
        break
    else:
        guess = int(guess)
        if guess == actual:
            print("Your guess is right!")
            break
        elif guess > actual:
            print("Your guess is too high. Try a smaller number.")
        elif guess < actual:
            print("Your guess is too small. Try a higher number.")