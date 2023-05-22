# Sequence 1
print("Sequence 1")
i = 0
num = 10.5
while i < 5:
    print(num)
    num -= 1
    i += 1
print("\n")

# Sequence 2
print("Sequence 2")
i = 0
num = 6
while i < 5: 
    print(f"{num} x {num} = {num*num}")
    num = num + 2
    i += 1
print("\n")

# Sequence 3
print("Sequence 3")
i = 0
while i < 5:
    if 14 % (i+1) == 0:
        print(f"{i+1} is a factor of 14")
    else:
        print(f"{i+1} is NOT a factor of 14")
    i += 1
