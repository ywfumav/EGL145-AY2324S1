# Setup
num1 = int(); num2 = int(); num3 = int()

# Input
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

# Process
if num1 > num2:
    if num1 > num3:
        print("The first number is the largest")
    else:
        print("The third number is the largest")
elif num2 > num1:
    if num2 > num3: 
        print("The second number is the largest")
    else: 
        print("The third number is the largest")