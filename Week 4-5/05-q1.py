# Question
# Write a simple calculator in Python which helps a supermarket customer to calculate 
# the total cost of unspecified fruits bought. The pseudocode and the console output 
# are given below. Choose suitable names for the variables used in the program. 

# Setup / Input
fruit = input("Enter the name of fruit bought: ")
qty = int(input(f"Enter the number of {fruit}'s bought: "))
price = float(input(f"Enter the price of a single {fruit}: "))

# Process
amt = qty * price

# Output
print(f"The amount to pay for the {fruit} is ${amt:.2f}")