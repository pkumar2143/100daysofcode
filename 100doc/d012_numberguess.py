import random
import sys

def difficulty_setting(difficulty_emh):
    if difficulty_emh == 'e':
        return 10
    elif difficulty_emh == 'm':
        return 6
    elif difficulty_emh == 'h':
        return 3
    else:
        return 10 # Default

def guess_checker(guess, target):
    if guess < target:
        print('Too Low')
        return False
    elif guess > target:
        print('Too High')
        return False
    else:
        print('********* YOU WIN!!!! *********')
        return True

print("++++++++++++++++++++++++++++++ Welcome to Number Guessing! ++++++++++++++++++++++++++++++")

min_value = 1
max_value = 100
TARGET_NUM = random.randint(min_value, max_value)

user_difficulty = str(input('Choose your Difficulty: [E]asy (Default), [M]edium, [H]ard \nYour choice: ')).lower()
num_guesses     = difficulty_setting(user_difficulty)

print(f"I'm thinking of a number between {min_value} and {max_value}\n")
print(f"You get {num_guesses} guesses to find it!\n")

guess_counter = 1
for i in range(num_guesses):
    print(f'Guess #{i + 1}')
    

    user_guess_error = True # In case user keeps entering some non-numeric.
    user_guess_error_counter = 0
    while user_guess_error:
        if user_guess_error_counter > 5:
            print("Too many erroneous entries... Stopping entire program!")
            sys.exit()
        try: 
            user_guess = int(input('Enter your guess: ')) # Assume user will enter an int
            user_guess_error = False
        except:
            user_guess_error_counter += 1
            print('Please enter a postive, whole number (e.g. 1, 2, 3, 4,...)')

    if guess_checker(user_guess, TARGET_NUM) == False:
        guess_counter += 1
        continue
    else:
        guess_counter += 1
        break

print("Guess Counter = ", guess_counter)
if guess_counter > num_guesses: # If you run out of guesses
    print(f"Correct Value = {TARGET_NUM}.\nBetter Luck Next Time!")



