# Question
# Write a program in Python that calculates the Body Mass Index (BMI) of a person. 
# The formula to calculate the BMI of a person is: 

# Setup / Input
name = input("Enter your name: ")
height = int(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

# Process
bmi = (weight / height / height) * 10000

# Output
print(f"Hi {name}, your BMI is {bmi:.1f}")