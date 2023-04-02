#Brady Fisher
#Rock Paper Scissors Game against the computer.
#Where the computer randomly selects what to "Throw"
import random

print("Welcome to the Rock, Paper, Scissors game")
gameOn = True
while(gameOn):

    #computer generated choice
    #Here 1 is Rock, 2 is Paper, and 3 is Scissors
    compChoice = random.randint(1,3)

    #player choice
    choiceGiven = False
    while(choiceGiven == False):
        playerChoice = str(input("What do you throw(Rock, Paper, or Scissors? "))
        playerCh = playerChoice.lower()
        pC = 0
        if(playerCh == "rock" or playerCh == "r"):
           pC = 1
           choiceGiven = True
        elif(playerCh == "paper" or playerCh == "p"):
           pC = 2
           choiceGiven = True
        elif(playerCh == "scissors" or playerCh == "scissor" or playerCh == "s"):
           pC = 3
           choiceGiven = True
        else:
            print("Invalid entry, please choose Rock, Paper or Scissors")

    #compare
    if(compChoice == 1):
            print("The computer played Rock")
            if(pC == 1):
                print("Tie, shoot again. :/")
            elif(pC == 2):
                print("You won!!! :)")                
                cont = True
                while(cont):
                    inp = str(input("Do you want to play again?" )).lower()
                    if(inp == "y" or inp == "yes" or inp == "yea" or inp == "yeah" or inp == "ya" or inp == "yup"):
                        print("Okay, play again")
                        cont = False
                    elif(inp == "n" or inp == "no" or inp == "nope" or inp == "nah"):
                        print("Okay, thanks for playing")
                        gameOn = False
                        cont = False
                    else:
                        print("Invalid response, please type yes or no.")
            elif(pC == 3):
                print("You lost :(")
                cont = True
                while(cont):
                    inp = str(input("Do you want to play again?" )).lower()
                    if(inp == "y" or inp == "yes" or inp == "yea" or inp == "yeah" or inp == "ya" or inp == "yup"):
                        print("Okay, play again")
                        cont = False
                    elif(inp == "n" or inp == "no" or inp == "nope" or inp == "nah"):
                        print("Okay, thanks for playing")
                        gameOn = False
                        cont = False
                    else:
                        print("Invalid response, please type yes or no.")

                
    if(compChoice == 2):
            print("The computer played Paper")
            if(pC == 1):
                print("You lost :(")                
                cont = True
                while(cont):
                    inp = str(input("Do you want to play again?" )).lower()
                    if(inp == "y" or inp == "yes" or inp == "yea" or inp == "yeah" or inp == "ya" or inp == "yup"):
                        print("Okay, play again")
                        cont = False
                    elif(inp == "n" or inp == "no" or inp == "nope" or inp == "nah"):
                        print("Okay, thanks for playing")
                        gameOn = False
                        cont = False
                    else:
                        print("Invalid response, please type yes or no.")
            elif(pC == 2):
                print("Tie, shoot again. :/")
            elif(pC == 3):
                print("You won!!! :)")
                cont = True
                while(cont):
                    inp = str(input("Do you want to play again?" )).lower()
                    if(inp == "y" or inp == "yes" or inp == "yea" or inp == "yeah" or inp == "ya" or inp == "yup"):
                        print("Okay, play again")
                        cont = False
                    elif(inp == "n" or inp == "no" or inp == "nope" or inp == "nah"):
                        print("Okay, thanks for playing")
                        gameOn = False
                        cont = False
                    else:
                        print("Invalid response, please type yes or no.")
                        
    if(compChoice == 3):
            print("The computer played Scissors")
            if(pC == 1):
                print("You won!!! :)")
                cont = True
                while(cont):
                    inp = str(input("Do you want to play again?" )).lower()
                    if(inp == "y" or inp == "yes" or inp == "yea" or inp == "yeah" or inp == "ya" or inp == "yup"):
                        print("Okay, play again")
                        cont = False
                    elif(inp == "n" or inp == "no" or inp == "nope" or inp == "nah"):
                        print("Okay, thanks for playing")
                        gameOn = False
                        cont = False
                    else:
                        print("Invalid response, please type yes or no.")
            elif(pC == 2):
                print("You lost :(")
                cont = True
                while(cont):
                    inp = str(input("Do you want to play again?" )).lower()
                    if(inp == "y" or inp == "yes" or inp == "yea" or inp == "yeah" or inp == "ya" or inp == "yup"):
                        print("Okay, play again")
                        cont = False
                    elif(inp == "n" or inp == "no" or inp == "nope" or inp == "nah"):
                        print("Okay, thanks for playing")
                        gameOn = False
                        cont = False
                    else:
                        print("Invalid response, please type yes or no.")
            elif(pC == 3):
                print("Tie, shoot again. :/")
            

        
                         
