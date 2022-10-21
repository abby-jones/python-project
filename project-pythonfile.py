another_event = bool(1)

while another_event == True:
    name = str(input("Hi there! Please enter your name: "))
    time = round(float(input("Please enter the time for your event in seconds to 2 d.p.: ")), 2)
    short = bool(input("Please enter '1' if this event was at a 25m pool. If it was in a 50m pool, enter '0'."))
    qual_time = round(float(input("Please enter the qualifying time for this event at your future competition in seconds to 2 d.p.: ")), 2)
    distance = int(input("Please enter the distance of your event in metres: "))
    stroke = str(input("Please enter the stroke of your event."))
    days_away = int(input("Please enter how manys are left until your competition"))

    if (0 < days_away < 3) == True:
        print("There is not long left until your competition.\nMake sure you keep rested to prevent any injuries.\nGood luck!")
    elif (3 <= days_away < 8) == True:
        print("In your final training sessions practice your turns, dives and finishes. Remember to eat well!")
    elif (8 <= days_away) == True:
        print("Push your volume in training as much as you can, at least 4km per 2 hour session. Keep grinding!")
    else:
        print("Error, invalid value entered, please try again.")

    option = int(input("Now please choose from the following options.\nEnter '1' to calculate your average 50m pace.\nEnter '2' to check if you qualify for this event.\nEnter '3' for your pool conversion time. "))
    if option == 1:
        lengths = distance/50
        pace = round((time/lengths), 2)
        print(f"Your average pace per 50m is {pace} seconds.")
    elif option == 2:
        diff = round((time - qual_time), 2)
        if diff > 0:
            print(f"You are currently {diff} seconds away from qualifying! Event cannot be entered.")
        elif diff == 0:
            print("You are exactly on the qualifying time! Make sure to get more practice in before competing.")
        else:
            print(f"Congratulations! You are {diff} seconds faster than the qualifying time.")
    elif option == 3:
        if short == True:
            long_time = round((time * 1.04), 2)
            print(f"Your converted 50m time for {distance} metres {stroke} is {long_time} seconds.")
        else:
            short_time = round((time / 1.04), 2)
            print(f"Your converted 25m time for {distance} metres {stroke} is {short_time} seconds")
    else:
        print("Invalid option selection, please try again.")

    another_event = bool(int(input("If you would like to enter another event, type '1'.\nIf you would like to exit the programme, type '0'.")))