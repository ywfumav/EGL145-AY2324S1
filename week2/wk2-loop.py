# for i in range(4):
#     print(f"i is {i}")

# # Declare
# i = 0

# # Process 
# while True:
#     print(f"i is {i}")
#     i = i + 1

    # if i == 100:
    #     break

# Guess the Random Number Game: 
from random import *

## Declare 
rand_num = randint(0,100)


## Input
guess = int(input("Please guess a number between 0 to 100: "))

while guess != rand_num:
    if guess > rand_num:
        print("You need to choose a lower number")
    else:
        print("You need to choose a higher number")
    
    guess = int(input("Good try...Please try again: "))

print(f"Your guess of {guess} is CORRECT!!!")