# Question
# Write a program that checks if a person has passed his physical fitness test.

gender = input("Enter the gender (Male / Female): ")
push = int(input("Enter the amount of push up: "))
sit = int(input("Enter the amount of sit up: "))

if gender == 'Male':
    if push >= 30 and sit >= 35:
        print("Passed Fitness Test")
    else:
        print("Failed Fitness Test")
else:
    if push >= 18 and sit >= 25:
        print("Passed Fitness Test")
    else:
        print("Failed Fitness Test")