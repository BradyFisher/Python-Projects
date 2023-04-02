#Brady Fisher
#Tic Tac Toe Game against the computer.
#Where the computer randomly places on any open space.
import random

def printBoard(oneVal,twoVal,threeVal,fourVal,fiveVal,sixVal,sevenVal,eightVal,nineVal):
    print("Placements are as follows: ")
    print(oneVal + " | " + twoVal + " | " + threeVal)
    print("---------")
    print(fourVal + " | " + fiveVal + " | " + sixVal)
    print("---------")
    print(sevenVal + " | " + eightVal + " | " + nineVal)
    


one = "1"
two = "2"
three = "3"
four = "4"
five = "5"
six = "6"
seven = "7"
eight = "8"
nine = "9"

#Visualization of Tic Tac Toe Board
printBoard(one,two,three,four,five,six,seven,eight,nine)


#Opening Coin Flip prompting for appropriate input
needOpeningGuess = True
while (needOpeningGuess):
    flipGuess = str(input("Guess Heads or Tails for the Coin flip (Enter H for Heads or T for Tails) "))
    if (flipGuess == "H") or (flipGuess == "T"):
        if flipGuess == "H":
            guess = 0
        else:
            guess = 1
        needOpeningGuess = False
    else:
        print("Please enter H for Heads or T for Tails ")

#Generate a coin flip Heads will be 0, and Tails will be 1    
flip = random.randint(0,1)
if(flip == 0):
    print("flip is Heads")
else:
    print("flip is Tails")




playerTurn = False
if(flip == guess):
    print("You won the coin Toss")

    needDecision = True
    while (needDecision):
        dec = str(input("Do you want to go first or second(1 for first, 2 for second "))
        if (dec == "1") or (dec == "2"):
            if dec == "1":
                playerTurn = True
            needDecision = False
        else:
            print("Please enter 1 for first or 2 for second ")

else:
    print("You lost the coin Toss")
    start = random.randint(1,2)
    if(start == 1):
        playerTurn = True
        print("The computer has decided to go second")
    else:
        print("The computer has decided to go first")






gameOver = False
playerbank = []
computerbank = []
possibles = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

while(gameOver == False):

    #PlayerTurn
    if(playerTurn):
        properPlay = False
        while (properPlay == False):
            printBoard(one,two,three,four,five,six,seven,eight,nine)
            play = str(input("Enter your placement "))
            if (play in possibles):
                playerbank.append(play)                
                possibles.remove(play)            
                playerTurn = False
                properPlay = True
                if play == "1":
                    one = "X"
                elif play == "2":
                    two = "X"
                elif play == "3":
                    three = "X"
                elif play == "4":
                    four = "X"
                elif play == "5":
                    five = "X"
                elif play == "6":
                    six = "X"
                elif play == "7":
                    seven = "X"
                elif play == "8":
                    eight = "X"
                else:
                    nine = "X"
            else:
                print("Please enter a possible play 1 through 9, that in not already played ")

    #ComputerTurn
    else:
        lengthOfPoss = (len(possibles) - 1)
        compPlay = random.randint(0,lengthOfPoss)
        play = possibles[compPlay]
        computerbank.append(play)
        possibles.remove(play)
        playerTurn = True
        print("The computer placed at "+ play)
        if play == "1":
            one = "O"
        elif play == "2":
            two = "O"
        elif play == "3":
            three = "O"
        elif play == "4":
            four = "O"
        elif play == "5":
            five = "O"
        elif play == "6":
            six = "O"
        elif play == "7":
            seven = "O"
        elif play == "8":
            eight = "O"
        else:
            nine = "O"
                      
    #check if game over
    if "1" in playerbank:
        if "2" in playerbank:
            if "3" in playerbank:
                gameOver = True
                printBoard(one,two,three,four,five,six,seven,eight,nine)
                print("You win!!")
        elif "4" in playerbank:
            if "7" in playerbank:
                gameOver = True
                printBoard(one,two,three,four,five,six,seven,eight,nine)
                print("You win!!")
        elif "5" in playerbank:
            if "9" in playerbank:
                gameOver = True
                printBoard(one,two,three,four,five,six,seven,eight,nine)
                print("You win!!")
    if "5" in playerbank:
        if "2" in playerbank:
            if "8" in playerbank:
                gameOver = True
                printBoard(one,two,three,four,five,six,seven,eight,nine)
                print("You win!!")
        elif "4" in playerbank:
            if "6" in playerbank:
                gameOver = True
                printBoard(one,two,three,four,five,six,seven,eight,nine)
                print("You win!!")
        elif "3" in playerbank:
            if "7" in playerbank:
                gameOver = True
                printBoard(one,two,three,four,five,six,seven,eight,nine)
                print("You win!!")
                
    if "9" in playerbank:
        if "3" in playerbank:
            if "6" in playerbank:
                gameOver = True
                printBoard(one,two,three,four,five,six,seven,eight,nine)
                print("You win!!")
        if "8" in playerbank:
            if "9" in playerbank:
                gameOver = True
                printBoard(one,two,three,four,five,six,seven,eight,nine)
                print("You win!!")

    if "1" in computerbank:
        if "2" in computerbank:
            if "3" in computerbank:
                gameOver = True
                printBoard(one,two,three,four,five,six,seven,eight,nine)
                print("You lose :( ")
        elif "4" in computerbank:
            if "7" in computerbank:
                gameOver = True
                printBoard(one,two,three,four,five,six,seven,eight,nine)
                print("You lose :( ")
        elif "5" in computerbank:
            if "9" in computerbank:
                gameOver = True
                printBoard(one,two,three,four,five,six,seven,eight,nine)
                print("You lose :( ")
    if "5" in computerbank:
        if "2" in computerbank:
            if "8" in computerbank:
                gameOver = True
                printBoard(one,two,three,four,five,six,seven,eight,nine)
                print("You lose :( ")
        elif "4" in computerbank:
            if "6" in computerbank:
                gameOver = True
                printBoard(one,two,three,four,five,six,seven,eight,nine)
                print("You lose :( ")
        elif "3" in computerbank:
            if "7" in computerbank:
                gameOver = True
                printBoard(one,two,three,four,five,six,seven,eight,nine)
                print("You lose :( ")
    if "9" in computerbank:
        if "3" in computerbank:
            if "6" in computerbank:                
                gameOver = True
                printBoard(one,two,three,four,five,six,seven,eight,nine)
                print("You lose :( ")
        if "8" in computerbank:
            if "7" in computerbank:
                gameOver = True
                printBoard(one,two,three,four,five,six,seven,eight,nine)
                print("You lose :( ")
                

    if(len(possibles) ==0):
        printBoard(one,two,three,four,five,six,seven,eight,nine)
        print("cat's scratch :/")
        gameOver = True
