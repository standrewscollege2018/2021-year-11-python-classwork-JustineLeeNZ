# guessing game

# set Boolean to keep asking until correct guess
keep_guessing = True


while keep_guessing == True:
    # ask for guess
    number = int(input("Enter a number between 1 and 10: "))

    # check guess
    if number == 6 :
        print("\nThat's right") 
        keep_guessing = False
    elif number > 6 :
        print("\nToo high, guess again")
    else:
        print("\nToo low, guess again")
        
        
print("Game over")



