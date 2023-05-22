# For Loop Version
# The average of all factors of a number provided by the user. 

num = int(input("Please enter a number: "))
count = 0
value = 0
for i in range(1, num+1):
    if num % i == 0:
        count += 1
        value = value + i

average = value / count 
print(f"The average of all factors for number {num} is {average:.2f}")