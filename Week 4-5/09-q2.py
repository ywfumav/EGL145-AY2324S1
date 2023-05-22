# Question
# Write a Python program that allows the user to guess a number between 1 and 10 
# that’s randomly generated. 

import random
answer = random.randint(1,10)

print("Generating a random number...")
num = int(input("Enter your guess: "))

while num != answer: 
    if num < answer:
        print("The answer is higher")
    else:
        print("The answer is lower")
    
    num = int(input("Enter your guess: "))

print("Correct!")