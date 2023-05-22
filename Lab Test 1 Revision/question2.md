# Lab Test 1 Reivision Question 2

## Section 1
Write a python program to accept user inputs for the following **fast food menu items**. Choose an appropriate **variable type** for each user input. 
1. `burger`
2. `fries`
3. `drinks`

### Console Output
```
Please enter the number of burger: 
Please enter the number of fries: 
Please enter the number of drinks: 
``` 

## Section 2 
The staff has commented that during peak hours, the program will **crash** if a staff accidentally keyed in a **non integer input** during operation. Reinforce your program by introducing **error handling capabilities** to prevent the program from crashing if the staff keyed in an **non integer input**. 

**Hint**: You can use a while loop for this operation
```
    while True:
        try:
            user_choice = int(input(f"Please enter the number of ____: "))
            break # Restart while loop when user input invalid statement
        except ValueError:
            print("Invalid Input, Please Try Again.")

```

### Console Output
```
Please enter the number of burger: 12 Burgers
Invalid Input, Please Try Again.
Please enter the number of burger: 12
Please enter the number of fries: 10
Please enter the number of drink: ddd
Invalid Input, Please Try Again. 
Please enter the number of drink: 11
```

**Bonus Challenge**: Try to write the `while loop` as a function to reduce repetition.

## Section 3
The restaurant is having a promotion now where customer will get to enjoy a special discount **if and only if** the condition fufil below:

* A **Meal** will consist of 1 x Burger, 1 x Fries and 1 x Drinks.
* A **Meal** will cost $10.

If the condition **does not fulfil**, the items will be charged individually
1. **Burger** will cost $8
2. **Fries** will cost $5
3. **Drinks** will cost $3

Write a algorithm to determine the quantity of eligible meals from the user input.
### Console Output
```
Please enter the number of burger: 10
Please enter the number of fries: 5
Please enter the number of drinks: 4
There are 4 meal, 6 burger, 1 fries and 0 drinks from the selection
```

## Section 4
Write a function, `calculate` to calculate the **total payable price** from the user input. The function, `calculate`, will take in 4 input arguments, namely,
1. meals qty
2. burger qty
3. fries qty
4. drinks qty

The function. `caclulate`, will also return one output argument, namely, `amt`.

### Console Output
```
Please enter the number of burger: 3
Please enter the number of fries: 2
Please enter the number of drinks: 1
There are 1 meal, 2 burger, 1 fries and 0 drinks from the selection
Total sum is $31
```