# Question
# First 100000 transactions made on a Friday using PayLah as entitles you to a 
# discount up to $3: 

# Setup / Input
first = input("First 100,000 transaction (True / False)?: ")
friday = input("Is it a Friday (True / False)?: ")
paylah = input("Is PayLah used (True / False)?: ")

if first == 'True' and friday == 'True' and paylah == 'True':
    print("You are entitled to a discount up to $3")
else:
    print("You are not entitled to a discount up to $3")