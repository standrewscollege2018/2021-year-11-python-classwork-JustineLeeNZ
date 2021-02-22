# simple for loop with input

# ask user how many names to enter
num_names = int(input("How many names do you wish to enter? "))


# ask for names
for i in range(0,num_names):
# ask user for their name
    name = input("Enter a name:\n")
    print("Hello {}\n".format(name))
