import random

print("Welcome to the number guessing game")
ans = random.randint(1, 100)
print(f"The ans is {ans}")
value = int(input("Enter a value: "))
checker = 'yes'

while checker == 'yes':
    while value != ans:
        if value < ans:
            print("Value is too low, Go Higher!")
        else:
            print("Value is too high, Go Lower!")
        value = int(input("Enter a value: "))

    print("Correct! Well Done! ")
    ans = random.randint(1, 100)
    checker = input("\nPlay again (Yes / No)?: ")
    checker = checker.lower()

print("Goodbye!")