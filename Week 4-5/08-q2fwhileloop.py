# While Loop Version
# The number of factors that the number 63 has.   

num = 63
count = 0
x = 1

while x < (num+1):
    if num % x == 0:
        count += 1
    x += 1

print(f"There are {count} factors for the number 63")