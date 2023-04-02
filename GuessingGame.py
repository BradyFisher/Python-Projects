#Brady Fisher
#A number guessing game.
#A random number between 0 and 99 is selected.
#Then players will take turns guessing the number.
#Can be played with Computer vs Computer, Human vs Computer, or Human vs Human.
#Where the computer randomly guesses a number between the high and low limits found by previous guesses.

import random

def checkForWin(guess, answer, player):
    print("You guessed ", guess, ". ")
    if (answer == guess):
        if(player == "p1"):
            print("You're right! Player1 wins!")
        else:
            print("You're right! Player2 wins!")
        return "Win"
    elif (answer < guess):
        print("Your guess is too high.")
        return "High"
    else:
        print("Your guess is too low.")
        return "Low"


def play():
    print("Who will play?")
    val = False
    while val == False:
        gameSetting = input("Options: Computer vs Computer (CC), Human vs Computer (HC) or Human vs Human (HH)")
        if gameSetting == "CC":
            player1 = ComputerPlayer()
            player2 = ComputerPlayer()
            val = True
        elif gameSetting == "HC":
            player1 = HumanPlayer()
            player2 = ComputerPlayer()
            val = True
        elif gameSetting == "HH":
            player1 = HumanPlayer()
            player2 = HumanPlayer()
            val = True
        else:
            print("Invalid input: Please enter CC, HC or HH to choose who will play)")
    
    guess = 0
    count = 0
    win = False
    answer = random.randint(0,99)
    lowLimit = 0
    highLimit = 99
    while (not win == "win"):
        print("Player 1's turn to guess:")
        guess = player1.getGuess(lowLimit, highLimit)
        win = checkForWin(guess, answer,"p1")
        if (win == "Win"):
            return
        elif win == "High":
            if(highLimit >= guess):
                highLimit = guess-1
        elif win == "Low":
            if(lowLimit <= guess):
                lowLimit = guess+1
        
        print("Player 2's turn to guess:")
        guess = player2.getGuess(lowLimit, highLimit)
        win = checkForWin(guess, answer,"p2")
        if (win == "Win"):
            return
        elif win == "High":
            if(highLimit >= guess):
                highLimit = guess-1
        elif win == "Low":
            if(lowLimit <= guess):
                lowLimit = guess+1

        
class Player(object):
    def getGuess(lowLim,highLim):
        raise NotImplementedError("Method: getGuess - not implemented")

class HumanPlayer(Player):
    def getGuess(self,lowLim,highLim):
        valid = False
        while valid == False:
            x = input("Enter your guess:")
            if not x.isnumeric():
                print("Invalid value entered. Guess must be a number between 0 and 99. Try again.")
            elif (int(x) >= 0) and (int(x) <= 99):
                valid = True
                return int(x)
            else:
                print("Invalid value entered:", int(x), "Guess must be between 0 and 99. Try again.")
                

class ComputerPlayer(Player):
    def getGuess(self,lowLim,highLim):
        x = random.randint(lowLim, highLim)
        return x

def main():
    play()

