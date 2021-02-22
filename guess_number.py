# guessing game

# get code to generate random numbers
import random

# set Boolean to keep asking until correct guess
keep_guessing = True

# set our number to guess
secret_number = random.randint(0,10)

# keep asking for guess until guess is correct
while keep_guessing == True:
    # ask for guess
    number = int(input("Enter a number between 1 and 10: "))

    # check guess
    # correct answer
    if number == secret_number :
        print("\nThat's right") 
        # stop asking for guesses
        keep_guessing = False
        
    # guess too high
    elif number > secret_number :
        print("\nToo high, guess again")
    
    # guess too low
    else:
        print("\nToo low, guess again")
        

# number successfully guessed, show game stats     
print("Game over")



