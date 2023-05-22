# For Loop Version
# The biggest factor of the number 70 (except for itself).

num = 70
factor = 0

for i in range(1, num):
    if num % i == 0:
        factor = i
    
print(f"The largest factor for number {num} is {factor}")
