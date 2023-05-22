# Question
# Write a Python program that checks if a person has passed his Japanese Language 
# Proficiency Test (JLPT) N5 Level.
# In order to pass
# (1) total score of both sections needs to be at or above the point required for 
# passing (overall pass mark), and, 
# (2)  score  in  each  scoring  section  needs  to  be  at  or above  the  minimum point 
# required for passing (sectional pass mark).

# Setup / Input
language = int(input("Enter the marks obtained in Language Section: "))
listen = int(input("Enter the marks obtained in Listening Section: "))

if language >= 38 and listen >= 19:
    total = language + listen
    if total >= 80:
        print("You passed the test")
    else:
        print("You failed the test")
else:
    print("You failed the test")