# Question
# Write a program that converts the temperature from Fahrenheit into Celsius and 
# Celsius into Fahrenheit.

# Setup / Input
temp = float(input("Enter the temperature: "))
choice = input("What scale is the temperature in (Fahrenheit / Celsius? ")

# Process 
if choice == 'Fahrenheit':
    convert = (temp - 32) * (5/9)
    scale = 'Fahrenheit'
else:
    convert = ((temp * (9/5)) + 32)
    scale = 'Celsius'

print(f"The temperature in {scale} is {convert:.3f}")