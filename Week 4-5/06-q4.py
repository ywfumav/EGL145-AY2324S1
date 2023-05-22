# Question
# Write a Python program to find the largest number out of three numbers accepted 
# from the user. You can assume that the user will always give three different numbers. 

# Setup / Input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Process / Output
if num1 > num2 and num1 > num3:
    print("The first number is the largest")
elif num2 > num1 and num2 > num3:
    print("The second number is the largest")
else: 
    print("The third number is the largest")