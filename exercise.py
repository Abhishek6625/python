import random

winning_num = random.randint(1,100)
guess = 1
number = int(input("Guess a number between 1 and 100 : "))
game_over = False

while not game_over:
    if number == winning_num:
        print(f"You win , and guesed this number in {guess} times ")
        game_over = True
    else:
        if number < winning_num:
            print("Too Low !")
            guess += 1
            number = int(input("Guess angin :"))  

        else:
            print("Too High ! ")
            guess += 1
            number = int(input("Guess again : "))    

