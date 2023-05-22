# Question
# Write a Python program that prompts the user to enter a number between 1 and 10, 
# inclusive. The program should then use a while loop to print the squares of all 
# numbers from 1 to the entered number (inclusive). 

num = int(input("Enter a number between 1 and 10: "))

while num > 10:
    print("Sorry, the number is out of range.")
    num = int(input("Enter a number between 1 and 10: "))

x = 1
while x <= num:
    print(x**2)
    x += 1