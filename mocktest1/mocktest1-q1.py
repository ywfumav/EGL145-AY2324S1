# FUNCTION
## Define function to convert km to miles 
def km2miles(num):

    value = (num * 0.621371) - ((num * 0.621371) % 0.01)
    return value

def miles2km(num):

    value = (num/0.621371) - ((num/0.621371) % 0.01)

    return value
    
# MAIN PROGRAM
## Setup 
km = float()
miles = float()

## Input
km = float(input("Enter distance(km): "))
## Process
miles = km2miles(km)
## Output
print(f"{km} km is {miles} miles.")

## Input
miles = float(input("Enter distance(miles): "))
## Process
km = miles2km(miles)
## Output
print(f"{miles} miles is {km:.2f} km.")