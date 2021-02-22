# guessing game

# set Boolean to keep asking until correct guess
keep_guessing = True


while keep_guessing == True:
    # ask for guess
    number = int(input("Enter a number"))

    # check guess
    if number == 6 :
        keep_guessing = False
    else:
        print("Wrong, guess again")



