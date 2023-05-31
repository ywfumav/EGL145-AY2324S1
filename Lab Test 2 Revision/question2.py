import random

print("Welcome to the number guessing game")
value = int(input("Enter a value: "))
ans = random.randint(1, 100)
print(f"The ans is {ans}")

while value != ans:
    if value < ans:
        print("Value is too low, Go Higher!")
    else:
        print("Value is too high, Go Lower!")
    value = int(input("Enter a value: "))

print("Correct! Well Done! ")
