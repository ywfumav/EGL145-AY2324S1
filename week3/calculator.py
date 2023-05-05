# Setup
nameOfTheFruit = str()
theNumberOfFruitsBought = int()
priceOfOneFruit = float()
totalAmountToPay = float()

# Input 
nameOfTheFruit = input("Enter the name of the fruit bought:")
theNumberOfFruitsBought = float(input(f"Enter the number of {nameOfTheFruit}:"))
priceOfOneFruit = float(input(f"Enter the price of a single {nameOfTheFruit}:"))

# Process
totalAmountToPay = theNumberOfFruitsBought * priceOfOneFruit

# Output 
if theNumberOfFruitsBought > 1:
    nameOfTheFruit = nameOfTheFruit + 's'
print(f"The amount to pay for the {nameOfTheFruit} is ${totalAmountToPay}")