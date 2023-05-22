# Question
# When given the number of sweets you have and the number of friends you 
# intend to share them equally with, the following program calculates the number of 
# sweets that is leftover after sharing. 

# Setup / Input
sweets = int(input("Enter the number of sweets you have: "))
friends = int(input("Enter the number of friends: "))

# Process
remain = sweets % friends

# Output
print(f"The number of sweets remaining after sharing is {remain}")