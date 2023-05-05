# Declare
qty = int(); price = float(); discount = float()
amt = float()
item = str()

# Input
qty = 500
price = 0.50
discount = 35
item = "Banana"

print(f"Qty is {qty}")
print(f"price is ${price}")
print(f"discount is {discount}%")
print(f"item is {item}")

# Process
amt = ((qty * price) * ((100 - discount)/100))
print(f"You are buying {qty} {item} and the total price is {amt:.10f}")
