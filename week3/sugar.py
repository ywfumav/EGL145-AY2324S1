# Setup
sugar = int()
volume = int()
rating = float()

# Input
sugar = int(input("Enter the amount of sugar found in the drink in grammes:"))
volume = int(input("Enter the volume of drink in ml:"))

# Process 
rating = sugar / volume
rating = rating * 100

# Output
if rating <= 1.0: 
    print("The beverage is rated A")
elif rating > 1.0 and rating <= 5.0:
    print("The beverage is rated B")
elif rating > 5.0 and rating <= 10.0:
    print("The beverage is rated C")
else: 
    print("The beverage is rated D")