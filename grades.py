# converts a mark to a grade

#ask the user for their mark
mark = int(input("Enter your mark"))

# tell user their grade
# check if mark is >= 0 and <= 100
if mark >= 0 and mark <= 100:
    # calculate grade
    # check if grade in A range
    if mark >= 90:
        print("A")
    # check if mark in B range
    elif mark >= 70:
        print("B")
    # check if mark in C range
    elif mark >= 50:
        print("C")
    # mark is a fail
    else:
        print("Fail")
    
    
else:
    print("Mark not eligible")







