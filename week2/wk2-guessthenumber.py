import random

Rand_num = random.randint(0, 100)
print(f"the random number is {Rand_num}")

guess = int(input("Please guess a number: "))

while Rand_num != guess:
    if guess > Rand_num:
        print("Go Lower")
    else:
        print("Go Higher")
    
    guess = int(input("Guess again!: "))
    
print("Correct!")