import random
user_input = int(input("Guess a number: "))
print(user_input)

magic_number = random.randint(0,10)
win = str("You win!!!")
lose = str("BZZZZZZZT!!! Wrong!! It was %d" % (magic_number))

if user_input == magic_number:
    print(win)

else:
    print(lose.upper())
