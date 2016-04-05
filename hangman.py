from __future__ import print_function
import random 


HANGMANPICS = ['''

 +---+
 |   |
     |
     |
     |
     |
     |
====== ''' , '''

 +---+
 |   |
 0   |
     |
     |
     |
     |
====== ''' , '''

 +---+
 |   |
 0   |
 |   |
     |
     |
     |
====== ''' , '''

  +---+
  |   |
  0   |
 /|   |
      |
      |
      |
======= ''' , '''

  +----+
  |    |
  0    |
 /|\   |
  |    |
       |
       |
======== ''' , '''
 +----+
  |    |
  0    |
 /|\   |
  |    |
 /     |
       |
======== ''' , '''

 +------+
  |     |
  0     |
 /|\    |
  |     |
 / \    |
        |
========= ''','''
 +------+
  |     |
  0     |
 /|\    |
  |     |
 / \    |  
0       |
========= ''', '''
+------+
  |     |
  0     |
 /|\    |
  |     |
 / \    |  
0   0   |
========= ''']

words = """ bear cat dog sheep lion tiger peacock horse crow parrot turkey emu weasel possum deer dingo fox minx skunk 
whale shark penguin cow buffalo bull hen pig lamb salmon tuna prawns crab lobster hoki herring sardine  """.split()

def getRandomWord(wordList):
#this function returns a random string from the words list
    wordIndex = random.choice(wordList)
    return wordIndex
    
def displayBoard(HANGMANPICS , missedLetters,correctLetters, secretWord):
    print (HANGMANPICS[len(missedLetters)])
    print() #give space after every string character
    
    print ('Missed letters: ', end = ' ')
    
            
    
    blanks = '_' * len(secretWord)
    #replace blanks with correct guesses
    for i in range (len(secretWord)): 
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks:
        print (letter, end=' ')
    print()
    
            


def getGuess(alreadyGuessed): #makes sure player enters a letter and nothing else
    while True:
        print ('Guess a letter.')
        guess = raw_input()
        guess = guess.lower()
        if len(guess) != 1:
            print ("please enter a single character.")
        elif guess in alreadyGuessed:
            print ("you have already guessed that letter. Choose another.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
           print ("please only enter a letter")
        else:
            return guess  #returns user i/p

#function is true if player wants to play again , else false

def playAgain():
    print ("do you wanna play again? (yes or no)")
    return raw_input().lower().startswith('y')


print ("<<<<<<<<<<< H A N G M A N >>>>>>>>>>>>")
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False 

while True:
    displayBoard(HANGMANPICS , missedLetters ,correctLetters, secretWord)
    #getting a letter from user
    guess = getGuess(missedLetters)
    

    if guess in secretWord:
        correctLetters = correctLetters + guess 
    
    #check if the player has won
    foundAllLetters = True 
    for i in range(len(secretWord)):
        if secretWord[i] not in correctLetters:
            foundAllLetters = False
            break 

    if foundAllLetters:
        print ("Yes! the secret word is "   + secretWord + "! You win!")
        gameIsDone = True 
    else:
        missedLetters = missedLetters + guess
              

#check if player has exhausted his guess limits and lost 

    if len(missedLetters) == len(HANGMANPICS)-1:
        displayBoard(HANGMANPICS , missedLetters , correctLetters , secretWord)
        print (" you have run out of guesses! \n After " + str(len(missedLetters)) + " missed guesses and  " + str(len(correctLetters)) 
        + " correct guesses  the word was  " + secretWord)  
        gameIsDone = True 
     
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False   
            secretWord = getRandomWord(words)
        else:
            break        
    
    










