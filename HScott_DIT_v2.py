# Title: Guess My Number v2
# Date: 01/04/2021
# Author: Hamish Scott
# Version: 2
""" The purpose of this code is to get the user to guess a preset number.
The code will tell them if the number is too high or too low and will
tell them if it is correct."""

# Setting up variables
import random
int_guess = 0
int_number = random.randint(1, 64)
int_num_of_guesses = 1


 
# Asks users name.
str_name = input('What is your name? ').title()

# User feedback loop, tells user if guess is too high or too low.
while int_guess != int_number:
    int_guess = int(input("Hi {}. Please try and guess \
the number between 1 and 64 inclusive: ".format(str_name)))
    if int_guess > int_number:
        print("{}, your guess is too high. Try again. ".format(str_name))
        int_num_of_guesses += 1
    elif int_guess < int_number:
        print("{}, your guess is too low. Try again. ".format(str_name))
        int_num_of_guesses += 1

# Prints how mant guesses user took.
print("Congratulations {}, you have guessed my number, \
you took {} guesses. Goodbye.".format(str_name, int_num_of_guesses))
