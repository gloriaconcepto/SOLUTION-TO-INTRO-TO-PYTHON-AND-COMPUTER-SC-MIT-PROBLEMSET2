#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mmk
#
# Created:     27/08/2018
# Copyright:   (c) mmk 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
import string
WORDLIST_FILENAME = "words.txt"
#===============================================================================
#FUNCTION TO RETURN TRUE IF WORD MATCH THE PATTERN OR OTHERWISE
#===============================================================================
def match_with_gaps(my_word,other_word):
    """ A FUNCTION Take two parameters (guess wrod,secret word),it return a boolean"""
    #we will only calls this methods when one has make at least two correct guesses
    #note that my_word will send for match if * is enter....
    match_counter =0
    new_my_word = my_word.replace(" ", "")
    print(new_my_word)
    is_word_contain_double=False
    #check if the word contains a double alphabet...
    for alp in new_my_word:

         if new_my_word.count(alp)>1 and alp != '_' :

            #then set the word contain double.. set is_word_contain_double=true
            is_word_contain_double=True

            #print(is_word_contain_double)
            #since it contain double letter
            break

    #check for each length
    if len(new_my_word)==len(other_word) and is_word_contain_double==False:


       for i in range(len(other_word)):
            if new_my_word[i]==other_word[i] or new_my_word[i] =='_':
                #print("hey am here")
                match_counter +=1

       if match_counter == len(other_word):
            return True
       else:
           print("length 2",len(other_word))
           return False

    else:
      print("double")
      return False

    #check if the word  appear twice in the secret word by returning a list:






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
#secret_word
    # Load the word.txt from the right directories
wordlist = load_words()
     #The secret word selected from word.txt file

    #secret_word=choose_word(wordlist)
secret_word=list("a")

if __name__ == "__main__":
    # pass

   # p1="ap ple"
    #p2="apple"
    #k1 = match_with_gaps(p1,p2)
    #print(k1)
