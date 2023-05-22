# Question
# Write a Python program with the following functionalities: 
## Find the total of two numbers given by the user, 
## Find the difference of two numbers given by the user, 
## Find the average of two numbers given by the user, and, 
## Quit the program. 

def function1(num1, num2):
    ans = num1 + num2

    return ans

def function2(num1, num2):
    ans = num1 - num2

    return ans

def function3(num1, num2):
    ans = (num1 + num2) /2 

    return ans


# Main Program
flag = False

while flag == False:
    print("What would you like to do today?")
    print("(1) Find the total of two numbers")
    print("(2) Find the difference of two numbers")
    print("(3) Find the average of two number")
    print("(Q) Quit")

    choice = input("Choose an option: ")

    if choice == '1':
        flag = True
    elif choice == '2':
        flag = True
    elif choice == '3':
        flag = True
    elif choice == 'Q':
        flag = True
    else:
        print("Sorry, your choice is invalid")

if choice == '1':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    ans = function1(num1, num2)
    print(f"The sum is {ans}")
elif choice == '2':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    ans = function2(num1, num2)
    print(f"The difference is {ans}")
elif choice == '3':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    ans = function3(num1, num2)
    print(f"The average is {ans}")
else:
    print("Thank you for using the program. Goodbye")
