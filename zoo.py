# figures out whether a person pays adult or child price at the zoo

# set child age to 13
CHILD_AGE = 13

# ask for age
age = int(input("How old are you?"))

# check age and display correct price
if age < CHILD_AGE :
    print("You pay the child price")
else:
    print("You pay the adult price")

print("Welcome to the zoo")





