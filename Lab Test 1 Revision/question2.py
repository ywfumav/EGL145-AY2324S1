def calculate(m, b, f, d):
    meal_price = 10
    burger_price = 8
    fries_price = 5
    drinks_price = 3

    amt = m * meal_price + b * burger_price + f * fries_price + d * drinks_price
    return amt

def user_choice(var):
    while True:
        try:
            result = int(input(f"Please enter the number of {var}: "))
            break # Restart while loop when user input invalid statement
        except ValueError:
            print("Invalid Input, Please Try Again.")
    return result

# Setup 
meal = 0

# Input
burger = user_choice('burger')
fries = user_choice('fries')
drinks = user_choice('drinks')

# Process
while burger > 0: 
    if fries > 0 and drinks > 0:
        meal += 1
        burger -= 1
        fries -= 1
        drinks -= 1
    else:
        break # exit the while loop

price = calculate(meal, burger, fries, drinks)

# Output
print(f"There are {meal} meal, {burger} burger, {fries} fries and {drinks} drinks from the selection")
print(f"Total sum is ${price}")
