import math

def convert(x):
    y = x * 0.0254

    return y

def areaRect(x, y):
    z = x * y

    return z

def areaCircle(r):
    area = math.pi * (r ** 2)
    return area

# Section 4
# Input
choice = int(input("Please select what do you like to do (1 - Area of Rect, 2 - Area of Circle, 3 - Exit): "))

# Process
if choice == 1:
    length = float(input("Please enter the length of the rectangle (inch): "))
    width = float(input("Please enter the width of the rectangle (inch): "))
    mlength = convert(length)
    mwidth = convert(width)
    area = areaRect(mlength, mwidth)
    print(f"Area of Rectangle is: {area} m2")

elif choice == 2:
    radius = float(input("Please enter radius (inch): "))
    print("Converting to meter...")
    print("Calculating area of circle...")
    mradius = convert(radius)
    area = areaCircle(mradius)
    print(f"Area of circle is: {area} m2")

else:
    print("Exiting program...")
    print("Have a nice day!")

# Section 3
# # Setup
# radius = float(); mradius = float(); area = float()

# # Input
# radius = float(input("Please enter radius (inch): "))
# print("Converting to meter...")
# print("Calculating area of circle...")

# # Process
# mradius = convert(radius)
# area = areaCircle(mradius)

# # Output
# print(f"Area of circle is: {area} m2")


# Section 2
# # Setup
# length = float()
# width = float()
# mlength = float()
# mwidth = float()

# # Input 
# length = float(input("Please enter the length of the rectangle (inch): "))
# width = float(input("Please enter the width of the rectangle (inch): "))

# # Process
# mlength = convert(length)
# mwidth = convert(width)
# area = areaRect(mlength, mwidth)

# #Output
# print(f"Area of Rectangle is: {area:.2f} m2")

# Section 1
# # Setup
# inch = float()
# meter = float()

# # Input
# inch = float(input("Please enter the dimension (inch): "))
# print("Converting to meters...")

# # Process
# meter = whatsup(inch)

# # Output
# print(f"Dimension meters is: {meter} m")
