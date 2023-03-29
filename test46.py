import random
l=["rock","scissor","papper"]

#rock vs papper->papper wins
#rock vs scissor-> rock wins
#papper vs scissor-> scissor wins.


while True:
    ccount=0
    ucount=0
    a=int(input('''
    game start......
    1 yes
    2 No| Exit 
    '''))
    if a ==1:
        for a in range(1,6):
            userInput=int(input('''
            1 rock
            2 scissor
            3 papper
            '''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="papper"
                Cchoice=random.choice(l)
            elif Cchoice==uchoice:
                print("computer Value",Cchoice)
                print("User Value",uchoice)
                print("game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=="rock" and Cchoice=="scissor") or (uchoice=="papper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="papper"):
                print("computer Value",Cchoice)
                print("user Value",uchoice)
                print("you win")
                ucount=ucount+1
            else:
                print("computer Value",Cchoice)
                print("user Value",uchoice)
                print("computer win")
                ccount=ccount+1
        if ucount==ccount:
            print("final game Draw.....")
            print("user score",ucount)
            print("computer Score",ccount)
        elif ucount==ccount:
            print("final you in  the game .....")
            print("user score",ucount)
            print("computer Score",ccount)
        else:
            print(" Computer you win The game.....")
            print("user score",ucount)
            print("computer Score",ccount)



    else:
        break;