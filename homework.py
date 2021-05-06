day = int(input('Day (0-6)?'))

if day == 0:
    print("Sunday")
elif day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")

if day == 0 or day == 6:
    print("It's the freakin weekend, baby!")
else: 
    print("Work work work... Something need doing?")