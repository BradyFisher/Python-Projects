#Brady Fisher
#Python Program to for a Hangman Game.
#Where a random word is selected from a List of 2020 Minnesota Twins player's Last names
#You are given the number of incorrect guesses equal to the length of the randomly selected word.

import random
from collections import Counter


words = '''garver astudillo avila sano gonzalez arraez adrianza donaldson kepler polanco cruz rosario cave buxton berrios ordorizzi maeda bailey dobnak smeltzer hill pineda rogers may duffey romo clippard'''

wordChoices = words.split(' ')
#randomy choose a word from the words list to use
word = random.choice(wordChoices)

if __name__ == '__main__':
    print('Guess the word. HINT: Last Name of a Minnesota Twins Player from 2020 Season')

    for i in word:
        print('_', end = ' ') 
    print()

    correct = False
    guessHistory = ''
    lettersGuessed = ''
    chances = len(word) 
    cor = 0
    flag = 0
    try:
        while(chances != 0) and flag == 0:
            print()

            try:
                guess = str(input('Enter a letter to guess: '))

            except:
                print('Enter only a letter!!')
                continue

            #Validation of the guess
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess.lower() in guessHistory:
                print('You have already guessed that letter')
                continue
            
            guessHistory = guessHistory + guess.lower()
            #If letter is guessed correctly
            if guess.lower() in word:
                k = word.count(guess)
                for _ in range(k):
                    lettersGuessed = lettersGuessed + guess.lower()
            else:
                chances = chances - 1

            #Print the word
            for char in word:
                if char in lettersGuessed and (Counter(lettersGuessed) != Counter(word)):
                    print(char, end = ' ')
                    correct = correct + 1
                elif(Counter(lettersGuessed) == Counter(word)):
                    print("The word is: ")
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break
                    break
                else:
                    print("_", end = ' ')

        if chances <= 0 and (Counter(lettersGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()
    
    
        
