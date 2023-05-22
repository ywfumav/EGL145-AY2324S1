# Sequence 1
print("Sequence 1")
for i in range(5):
    print(i)
print("\n")

# Sequence 2
print("Sequence 2")
num = 33
for i in range(5):
    print(num)
    num = num - 11
print("\n")

# Sequence 3
print("Sequence 3")
for i in range(5):
    if (i+1) % 2 == 0: 
        print(f"{i+1} is even")
    else:
        print(f"{i+1} is odd")
print("\n")

# Sequence 4
print("Sequence 4")
for i in range(5):
    if 12 % (i+1) == 0:
        print(f"{i+1} is a factor of 12")
    else:
        print(f"{i+1} is NOT a factor of 12")