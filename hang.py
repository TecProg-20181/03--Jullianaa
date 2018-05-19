import random
import string
import os.path

WORDLIST_FILENAME = "palavras.txt"

class Word():
    def __init__(self):
        self.infile = ""
        self.line = ""
        self.wordlist = ""

    def loadwords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        if os.path.isfile(WORDLIST_FILENAME):
            print "Loading word list from file..."
            inFile = open(WORDLIST_FILENAME, 'r', 0)
            line = inFile.readline()
            wordlist = string.split(line)
            print "  ", len(wordlist), "words loaded."
            return random.choice(wordlist)
        else:
            print "File ", WORDLIST_FILENAME, "not found!"


def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getGuessedWord():

     guessed = ''


     return guessed

def getAvailableLetters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase
    
    return available

def printWelcome(secretWord):
    print('Welcome to the game, Hangam!')
    print('I am thinking of a word that is', len(secretWord), ' letters long.')
    print('-------------')

def hangman(secretWord):

    guesses = 8
    lettersGuessed = []
    printWelcome(secretWord)
    
    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
        print('You have ', guesses, 'guesses left.')

        available = getAvailableLetters()
        auxAvailable = getAvailableLetters()

        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print('Available letters', available)
        letter = raw_input('Please guess a letter: ')
        while letter.__len__() > 1 or letter not in auxAvailable:
                print '\nHeeeeey, attention!\n'
                print 'You only need ONE letter at this moment!'
                print 'Available letters', available
                letter = raw_input('Please guess a letter: ')

        if letter in lettersGuessed:

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print('Oops! You have already guessed that letter: ', guessed)
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print('Good Guess: ', guessed)
        else:
            guesses -=1
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print('Oops! That letter is not in my word: ',  guessed)
        print('------------')

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('Congratulations, you won!')
        else:
            print('Sorry, you ran out of guesses. The word was ', secretWord, '.')
            cont = raw_input("Input 'yes' to continue tring.")
            while(cont == 'yes'):
                print("\n\n\nHEEEEEY, COMO ON!")
                hangman(secretWord)

word =  Word()
secretWord = word.loadwords().lower()
hangman(secretWord)
