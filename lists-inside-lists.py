# examples of lists inside lists

# *** create a master list that contains other sub-lists ***
# the master list starts and ends with [] brackets which all the sublists sit inside
# each sub-list must be enclosed in [] brackets with commas between the [] brackets
# items inside each sub-list are separated by commas
# list of client details
client_list = [["John Smith",16],["Bob O'Roberts",18]]

# *** print an entire sublist ***
# print first client
# note the [] and commas - UGLY - only use this for debugging
print(client_list[0])

# *** print an individual sub-list item ***
# print the name of the first client
print(client_list[0][0])

# print the age of the first client
print(client_list[0][1])

# print the name of the second client
print(client_list[1][0])

# print the age of the second client
print(client_list[1][1])


# *** ask user for an index and print client details for that sub-list ***
# ask user for input
index = int(input("Enter a number: "))

# print client name
print(client_list[index][0])

# print client age
print(client_list[index][1])

# print name and age with nice formatting
print("Name: {} Age: {}".format(client_list[index][0], client_list[index][1]))



# *** print each name and age from the list ***
# range starts at zero and uses length of list for stop value
# use index variable to select next sub-list each time for loop runs
# use actual numbers to specify item inside sub-list e.g. name has index 0
for index in range(0, len(client_list)):
    print(client_list[index][0], client_list[index][1])


# *** print a numbered list ***
# use index+1 to print numbered list
# use .format() to combine variable values and unchanging text
for index in range(0, len(client_list)):
    print("{}. Name: {} Age: {}".format(index+1, client_list[index][0], client_list[index][1]))

# *** add new client ***
# ask user for client details
name = input("Enter client name: ")
age = int(input("Enter client age: "))

# use append() to add new client details as sub-list
# variables with new info need to be enclosed in [] brackets
client_list.append([name,age])

# print entire list to check new client added
print(client_list)

# *** delete an entire client sub-list ***
# ask user for index of sub-list to delete
index = int(input("Enter index of client to delete: "))

# delete sub-list that matches specified index
# note that del comes before the listname and there is a space between them
del client_list[index]

# print entire list to check client deleted
print(client_list)

# *** update existing client details ***
# update name for first client
client_list[0][0] = "Jenny Smith"

# print entire list to check client name updated
print(client_list)

# update age for first client
client_list[0][1] = 100

# print entire list to check client age updated
print(client_list)
