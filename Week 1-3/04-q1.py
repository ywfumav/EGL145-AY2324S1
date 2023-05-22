# Question
# Write a "Guess the number" game
# The program will use the library RANDOM to generate a random integer number between 0 - 100.
# User will input an integer value, program will indicate whether the input is a correct/incorrect guess.
import random

# Setup / Input
rand = random.randint(0, 100) # Generate a random integer between 0 to 100
check = False 

# Process / Output
while check == False:
    guess = int(input("Enter a number: "))
    
    if guess == rand:
        check = True
        print("Correct!")
    elif guess < rand:
        print("The answer is higher")
    else:
        print("The answer is smaller")