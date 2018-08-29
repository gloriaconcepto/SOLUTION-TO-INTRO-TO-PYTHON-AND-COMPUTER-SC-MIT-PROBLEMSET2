#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mmk
#
# Created:     24/08/2018
# Copyright:   (c) mmk 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
                         #-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mmk
#
# Created:     23/08/2018
# Copyright:   (c) mmk 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""lambda,map&filters,generators,class static methods,comprehensims,Mro concept"""
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


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"


    available_letters = string.ascii_lowercase

    for letter in letters_guessed:

        available_letters = available_letters.replace(letter, "")

    return available_letters

#==============================================================================
# CODE FOR THE HANGMAN PART 2
#===============================================================================

def hang_man_part():
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    #secret_word
    # Load the word.txt from the right directories
    wordlist = load_words()
     #The secret word selected from word.txt file

    #secret_word=choose_word(wordlist)
    secret_word=list("apple")

    #temp_data_list2=["_ "] * len(secret_word)
    temp_string=["_  "] * len(secret_word)

    #create a second  temporary list
    data_list2 = "".join(temp_string)

    #number of guesses
    num_guess = int(6)

    #how many letters the secret_word contains
    print("Welcome to the game Hangman!")

    print("I am thinking of a word that is",len(secret_word) ," letters long.")


   # has the word been in the secret word before
    num_of_time_word_in_scretword=0

   #warning for wrong input
    wrong_input_warning=3

    #list to hold all the letter that have been
    list_to_store_guess_letter =[]
   #create a boolean to check if the word has enter the loop to check for a word.
    hav_we_enter_loop=False
   #start counting the number of loop

    while num_guess > 0 :

        print ("You have",wrong_input_warning,"warnings left.")
        #play the game and also check if it is True
        print("You have", num_guess, "guesses left")

        #show avialable word present
        if num_guess==6:
         print("Available letters: ",string.ascii_lowercase)
        else:
           print("Available letters: ",get_available_letters(letters_guessed))

        #start playing the game
        enter_a_letter = input("Please  guess a letter :  ")
        #letters_guessed = list(input("Please  guess a letter :  "))

        #check if it is a string
        if enter_a_letter.isalpha() and enter_a_letter not in list_to_store_guess_letter:

          letters_guessed=list(enter_a_letter.lower())

          # add the guess word to the list
          list_to_store_guess_letter.append(enter_a_letter)

        #transverse the list:
          for i in letters_guessed:

             if i in secret_word:
                #letters_guessed.append(users_guess)
                if num_of_time_word_in_scretword==0:

                  temp_string =get_guessed_word(secret_word, letters_guessed)

                  #convert from string to a temporary list to hold the data...

                  data_list1 =list(temp_string.replace(" ", ""))

                  print("Good Guess1:",temp_string)

                  data_list2 ="".join(temp_string)

                  num_of_time_word_in_scretword +=1
                  hav_we_enter_loop=True

                else:
                     for (index,val) in enumerate(secret_word):
                        #if i not in temp_data_list2:
                         if i==val :

                            data_list1[index]=i

                            #crete a second temporary data link list

                            data_list2 = "".join(data_list1)


                            num_of_time_word_in_scretword = 5

                     print("Good Guess2:",data_list2)
                     hav_we_enter_loop=True

                #go through
               # print("Good Guess:",temp_data_list2 )
                print("__________________________________________")
           #don't reduced the guess....
           #condition to check if there is still space in the secret_word to set False:
             else:
            #check for wrong word ,decrease guess count set:


            # print("Oops! That letter is not in my word:", hey)
              if num_of_time_word_in_scretword<2:
                   data_list2 ="".join(temp_string)

                   if num_of_time_word_in_scretword==0:
                    print("Oops! That letter  is not in my word:",data_list2 )
               # else:
                   if num_guess<4:
                     print("Oops! That letter  is not in my word:",data_list2 )
              else:
                    print("Available letters: ",get_available_letters(letters_guessed))

                    print("Oops! That letter is  not in my word:", data_list2)

              num_guess -=1
        else:
            #subtract the warnig  and also check if the warning is zero
            if  wrong_input_warning <=0:
                # reduce the number of guesses
                num_guess -=1
            else:
                wrong_input_warning -=1
                if enter_a_letter in list_to_store_guess_letter and hav_we_enter_loop:
                         print ("Oops! You've already guessed that letter. You now have",wrong_input_warning,"warnings left:",data_list2)




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #enter the guess word
   # letters_guessed = list(input("Please enter the guess word :  "))
   #letters_guessed = ['e','i','k','p','r','s']
   #print(get_available_letters(letters_guessed))
   hang_man_part()