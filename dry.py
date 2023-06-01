
winning_num = 55
guess = 1
game_over = False

while True:
    number = int(input("Guess a number between 1 and 100 : "))
    if number == winning_num:
        print(f"You win , and guesed this number in {guess} times ")
        break
    else:
        if number < winning_num:
            print("Too Low !")

        else:
            print("Too High ! ")


        guess += 1
        continue       
            
              