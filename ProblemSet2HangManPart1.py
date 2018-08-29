#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mmk
#
# Created:     20/08/2018
# Copyright:   (c) mmk 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import string
WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word ,letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
   #pass
     #counter
    counter = 0
    #code below added here by me...

     #lambda expression to change  word in list to lower case
    lower_case_word =[x.lower() for x in letters_guessed ]
    #transverse through the loop to check if it is in the secret word
    for i in lower_case_word:
        if i in secret_word:
           # if char == i:
          counter +=1
          #print(counter)


    #check if the length of secret_word  matches counter number
    if counter==len(secret_word):
        return True
    else :
        return False


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #the_secret_word = choose_word(wordlist)
    the_secret_word ="apple"
    #hangman(secret_word)
     #enter the guess word
    letters_guessed = list(input("Please enter the guess word :  "))
    print(is_word_guessed(the_secret_word,letters_guessed))
