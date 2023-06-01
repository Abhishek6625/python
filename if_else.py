winning_num = 27

user_input = int(input("Guess a number b/w 1 and 100 : "))

if user_input == winning_num :
    print("you win !!!!")

else :
    if user_input < winning_num :
        print("Too low !")

    else :
        print("Too High !")    