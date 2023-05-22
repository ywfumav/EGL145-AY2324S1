# For Loop Version
# The biggest factor of the number 70 (except for itself).

num = 70
factor = 0
x = 1

while x < (num):
    if num % x == 0:
        factor = x
    x += 1
    
print(f"The largest factor for number {num} is {factor}")
