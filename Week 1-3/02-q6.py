# Question
# The following program calculates the amount of money the customer needs 
# to pay for an unspecified item after given a discount input by the cashier.

# Setup / Input
item = input("Enter the name of the item to be bought: ")
qty = int(input(f"Enter the number of {item}'s bought: "))
price = float(input(f"Enter the price of a single {item}: "))
discount = float(input(f"Enter the percentage discount: "))

# Process
amt = (qty * price) * ((100 - discount) / 100)

# Output
print(f"Please pay ${amt} for the {item}s")