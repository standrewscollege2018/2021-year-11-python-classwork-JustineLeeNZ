# examples of list basics

import random

my_numbers = [2,4,6,8,10,12]

my_names = ["Bryn", "Justine", "Meredith", "Rhys", "Ash"]

my_prices = [12.5, 45.6, 77.0, 121.3]

print(my_prices[0])
print(my_names[2])
print(my_numbers[5])

# use a random number to get info out of a list
number = random.randint(0,3)
print(my_names[number])

# finding length of a list
print("list is my_names")
print(len(my_names))

print("list is my_numbers")
print(len(my_numbers))

print("list is my_names")
print(len(my_prices))

# change something in list
print(my_prices)
my_prices[1] = 55.5
print(my_prices)

my_names[1] = "Ms Lee"
print(my_names)

# add a new value to the end of the list
my_names.append("Ewan")
print(my_names)

my_names.append("Sophie")
print(my_names)





