# For Loop Version
# The number of factors that the number 63 has.   

num = 63
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count += 1

print(f"There are {count} factors for the number 63")