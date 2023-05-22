# While Loop Version
# The average of all factors of a number provided by the user. 

num = int(input("Please enter a number: "))
count = 0
value = 0
x = 1

while x < (num + 1):
    if num % x == 0:
        count += 1
        value = value + x
    x += 1

average = value / count 
print(f"The average of all factors for number {num} is {average:.2f}")