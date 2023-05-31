import math 

def areaofCircle(x):
    area = math.pi * x * x 
    return area

# Main Program
# Setup / Input
start = int(input("Please enter starting number: "))
end = int(input("Please enter ending number: "))
print(f"Number ranging from {start} to {end}")

for i in range(start, end+1):
    area = areaofCircle(i)
    print(f"Area of circle radius {i} is {area:.03f}")