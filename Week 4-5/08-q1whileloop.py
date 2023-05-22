# While Loop Version
# The total of all even numbers between 2 numbers provided by the user. 

# Setup / Input
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

if num1 < num2:
    x = num1 
    y = num2
else:
    x = num2
    y = num1

# Process / Output
count = 0
num = x
while num < (y+1):
    if num % 2 == 0:
        count += 1
    num += 1

print(f"There are {count} even number from {x} to {y}")