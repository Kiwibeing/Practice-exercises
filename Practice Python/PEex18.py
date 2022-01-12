# Cows and bulls: Create a program that will play the “cows and bulls” game with the user. The game works like this: 
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

import random

# Something to improve on:
def compare_numbers(number,guess):
    cowbull = [0, 0] # [cows,bulls]
    # Use this instead!
    for i in range(len(guess)):
        if guess[i] == number[i]:
            cowbull[0] += 1
        else:
            cowbull[1] += 1

    return cowbull


if __name__ =='__main__':
    counter = 0
    print("Welcome to the Cows and Bulls Game! Guess a 4 digit number!")
    number = str(random.randint(1000, 9999))
    while True:
        guess = input("Enter a number:\n>>> ")
        cows_count, bulls_count = 0, 0
        i = 0
        if guess == 'exit':
            break
        for j in number:
            if j == guess[i]:
                cows_count += 1
            else:
                bulls_count += 1
            i += 1
        counter += 1
        print(f'{cows_count} cows, {bulls_count} bull')
        print(f'{counter} tries')
        if guess == number:
            print(f"Congrats, you have guess correctly in {counter} tries!")
            break