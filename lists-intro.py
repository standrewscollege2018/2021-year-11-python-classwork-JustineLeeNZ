# This program demonstrates how lists work

# For lists, we use square brackets
# Items in lists are separated by commas
# String needs to have speech marks around it
names = ["Josh","Sophie"]

# To print a list
print(names)

# To print an individual item from a list, we use
# its index (position in the list)
print(names[1])

# To add something to the end of a list, use append()
names.append("Dr Evil")
print(names)


# To add something in a specific position, use insert()
names.insert(1, "Jamie")
print(names)


# Lists are mutable (changeable)
# To change the value of an item in a list, we just
# over-write it
names[3] = "Dr Who"
print(names)

# len(list) returns the number of items in a list
print(len(names))


# There are two ways we can loop through a list to
# print out the items

# 1. a simple for loop with no range
for current_name in names :
    print(current_name)


# 2. Use range() to get numbered list
# Use len(list) to get how many times to loop
for index in range(0,len(names)):
    print("{}. {}".format(index+1, names[index]))

names.append("Iron Man")

for index in range(0,len(names)):
    print("{}. {}".format(index+1, names[index]))



