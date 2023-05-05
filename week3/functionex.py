def Function1(num1, num2, num3):
    ans = num1 + num2 + num3
    print("In function 1")
    print(f"num 1 is {num1}, num 2 is {num2} and num 3 is {num3}")
    return ans

def Function2(num1, num2, num3):
    ans = num1 - num2 - num3
    print("In function 2")
    print(f"num 1 is {num1}, num 2 is {num2} and num 3 is {num3}")
    return ans

def Function3(num1, num2, num3):
    ans = num1 * num2 * num3
    print("In function 3")
    print(f"num 1 is {num1}, num 2 is {num2} and num 3 is {num3}")
    return ans

def Function4(num1, num2, num3):
    ans = num1 / num2 / num3
    print("In function 4")
    print(f"num 1 is {num1}, num 2 is {num2} and num 3 is {num3}")
    return ans

# Main Program
w = -1
x = 1
y = 2
z = 3

# Process & Output 
value1 = Function1(w, x, y)
print(f"Value 1 is {value1}\n")

value2 = Function2(y, x, w)
print(f"Value 2 is {value2}\n")

value3 = Function3(z, z, z)
print(f"Value 3 is {value3}\n")

value4 = Function4(y, x, y)
print(f"Value 4 is {value4}\n")




