''' uses weight and age to calculate correct dose of paracetemol '''

# constants
AGE_LIMIT = 12
DOSE_PER_KG = 10

# ask for age
age = float(input("Enter your age: "))

# check age to see whether also need weight

# child dose
if age < 12 :
    # ask for weight
    weight = float(input("Enter your weight: "))

    # calculate dose - convert dose to string so can add units
    dose = str(DOSE_PER_KG * weight) + " milligrams"


# adult dose
else:
    dose = "2 x 500mg tablets"

# display dose info
print("Recommended dose every 4-6 hours is {}".format(dose))

