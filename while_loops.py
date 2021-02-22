# while loops examples

# while as counter (for loop better!)
# set counter to initial value
number = 0

while number < 10:
    print(number)
    number = number + 1

# when loop finished, print final msg
print("All done!")


# while loop to check for correct name
# set Boolean to True
keep_asking = True

# start asking their name
while keep_asking == True:
    # ask for their name
    name = input("Enter your name")

    # if correct name
    if name == "Jaime":
        keep_asking = False

    # wrong name
    else :
        print("Wrong name")

# loop finishes, greet Henry
print("Hi Jaime")




