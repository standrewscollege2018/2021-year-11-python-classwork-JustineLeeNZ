# guessing game

# get code to generate random numbers
import random

# set Boolean to keep asking until correct guess
keep_guessing = True

# set our number to guess
secret_number = random.randint(0,10)

while keep_guessing == True:
    # ask for guess
    number = int(input("Enter a number between 1 and 10: "))

    # check guess
    if number == secret_number :
        print("\nThat's right") 
        keep_guessing = False
    elif number > secret_number :
        print("\nToo high, guess again")
    else:
        print("\nToo low, guess again")
        
        
print("Game over")



