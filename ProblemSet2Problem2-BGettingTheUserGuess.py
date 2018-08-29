#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mmk
#
# Created:     22/08/2018
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


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
     #counter
    counter = 0
    #code below added here by me...
    #temp_data_list=list(secret_word[:])
    temp_data_list=["_ "] * len(secret_word)
    che_data_list =[]
    #print(secret_word)
    #transverse through the loop to check if it is in the secret word
    for (i,val) in enumerate(letters_guessed):
        if val in secret_word:
            #check if how many times the word is in the temporary data list.
            if val in che_data_list:
                 counter +=1

            else:
           # add the word in a temporary data structure.

             counter +=1

            num_data_list =[i  for i,v in enumerate(secret_word) if v==val]
            #go the length and add it and the right position
            for num in num_data_list:
                 temp_data_list[num] = val

            #add to the che_data_list
            che_data_list.append(val)
        #else :
           #adding the default underscore
           #temp_data_list[i] = "_ "
         #  print("hey")


    #check if the length of secret_word  matches counter number
    if counter==len(secret_word):
        return "".join(temp_data_list)
    else :
        #return print("Hey sorry player no such word exist in the secret word.wrong guess")
        return "".join(temp_data_list)


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #the_secret_word = choose_word(wordlist)
    the_secret_word ="apple"
    #hangman(secret_word)
     #enter the guess word
    letters_guessed = list(input("Please enter the guess word :  "))
   # letters_guessed = ['e','i','k','p','r','s']
    print ( get_guessed_word(the_secret_word , letters_guessed) )