# try-except examples

# ask user for number, check is an integer

try:
    value = int(input("Enter a number: "))
    print(value)
except:
    print("Error: invalid data type")


# example with a loop

keep_asking = True

while keep_asking == True:
    try:
        value = int(input("Enter a number: "))
        keep_asking = False
    except:
        print("Error: invalid data type")

print(value)
