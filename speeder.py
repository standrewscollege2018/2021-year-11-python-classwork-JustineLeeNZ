# system for police officer who catches speeders

keep_asking = True
while keep_asking:
    name = input("Enter a name")
    if name == "end" :
        keep_asking = False
    else:
        speed_limit = int(input("Enter current limit"))
        current_speed = int(input("Enter speed"))

        if current_speed - speed_limit > 29 :
            print("Fine is $180")
        elif current_speed - speed_limit >= 19 :
            print("Fine is $130")
        elif current_speed - speed_limit >= 10 :
            print("Fine is $80")
        else:
            print("Fine is $30")
