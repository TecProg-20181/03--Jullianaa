import random
import string

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
        print "Loading word list from file..."
        # inFile: file
        self.infile = open(WORDLIST_FILENAME, 'r', 0)
        # line: string
        self.line = self.infile.readline()
        # wordlist: list of strings
        self.wordlist = string.split(self.line)
        print "  ", len(self.wordlist), "words loaded."
        return random.choice(self.wordlist)


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
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print('Available letters', available)
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
