# decides whether person is eligible to be donor

# constants
MIN_AGE = 18
MIN_WEIGHT = 45


# ask user for age and weight
age = int(input("Enter your age: "))
weight = int(input("Enter your weight in kg: "))

# check if eligible to be donor
# both age and weight must OK to be eligible

if age >= MIN_AGE and weight >= MIN_WEIGHT :
    print("You are eligibile")
else:
    print("You are not eligible")


