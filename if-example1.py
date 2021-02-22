# use if statements to make decisions in code

# ask user for their age
age = int(input("What is your age?"))

# check if person is old enough to drive
if age >= 16 :
    print("You can get your driver's licence")
else:
    print("You will be old enough in {} year(s)".format(16-age))
