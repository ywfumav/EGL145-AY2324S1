# # Declare
# member = int()
# spend = int()

# # Input
# member = int(input("Can you enter your membership status (1 is True | 0 is False): "))
# spend = int(input("Have you spend more than $50? (1 is True | 0 is False): "))
# print(f"Member is {member} and the type is {type(member)}") 
# print(f"Spend is {spend} and the type is {type(spend)}")

# # Declare / Input (1 is True | 0 is False)
# member = int(input("Please enter if user is member (1 is True | 0 is Fales): "))
# spend = int(input("Has the user spend more than $50 (1 is True | 0 is Fales): "))

# # print(f"User input member is {member} {type(member)} and spend is {spend} {type(spend)}")
# # Process
# if member == 1 and spend == 1:
#     print("You are entitled to a discount")
# else:
#     print("Please get out")








# Declare / Input
member = input("Are you a member (True/False)?: ")
spend = input("Have you spent more than $50 (True/False)?: ")

member = member.lower()
spend = spend.lower()

if member == "true":
    member = bool(True)
else:
    member = bool(False)

if spend == "true":
    spend = bool(True)
else:
    spend = bool(False)

print(f"Member is {member} and the type is {type(member)}")
print(f"Spend is {spend} and the type is {type(spend)}")

# Process
if member or spend: 
    print("You are eligible for discount")
else:
    print("You are not eligible for discount")
    
# if member == "True":
#     member = bool(True)
# else:
#     member = bool(False)

# if spend == "True":
#     spend = bool(True)
# else:
#     spend = bool(False)

# print(f"Member is {member} and the type is {type(member)}")
# print(f"Spend is {spend} and the type is {type(spend)}")

# # Process
# if member or spend: 
#     print("You are eligible for discount")
# else:
#     print("You are not eligible for discount")



# # Boolean
# member = member.lower() == 'true'
# spend = spend.lower() == 'true'


# if member and spend: 
#     print("You are eligible for discount")
# else:
#     print("You are not eligible for discount")