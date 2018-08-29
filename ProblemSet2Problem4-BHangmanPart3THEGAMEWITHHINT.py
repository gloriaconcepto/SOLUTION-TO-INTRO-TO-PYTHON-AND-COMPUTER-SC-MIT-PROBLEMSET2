#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mmk
#
# Created:     28/08/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------
import random
import string
import re
WORDLIST_FILENAME = "words.txt"
#===============================================================================
#  FUNCTION TO DISPLAY SCORE WHEN ONE HAVE WON THE GAME
#===============================================================================
def display_score_won_game(enter_list,word,guess_num,letter_guess):

    if len(enter_list) ==len(word) and '_' not in enter_list:
        print("Congratulations, you won!")
        #calculate the game score
        temp_unique_num=pos_in_secret_word(word,letter_guess.lower())

        number_unique_letters_in_secret_word =temp_unique_num[len(temp_unique_num)-1]

        total_score = guess_num * number_unique_letters_in_secret_word

        print("Your total score for this game is: ",total_score)

        #Terminate the while loop
        guess_num = -7
        print(guess_num)




#===============================================================================
# FUNCTION TO GET  GUESSED WORD
#===============================================================================
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

#===============================================================================
# FUNCTION TO GET THE AVAILABLE LETTERS
#===============================================================================
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

#===============================================================================
#   FUNCTION FOR DETERMINING THE POSITION OF LETTER IN SECRET WORD
#===============================================================================
def pos_in_secret_word(secret_word,alphabet):
    """ This function tells us the index position a word is in the secret word"""
    #convert it to a list
    list_word = list(secret_word)
    empty_list=[]
    for i,v in enumerate(list_word):
        #empty_list[i]=i+1
        #check all the number the guess word is in the secret word
        if v== alphabet:
         empty_list.append(i+1)

    return empty_list
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
     # print("double")
      return False

    #check if the word  appear twice in the secret word by returning a list:

#====================================================================================
# FUNCTION TO SHOW ALL POSSIBLES MATCHES
#===============================================================================

def show_possible_matches(secret_word1):
     #guess_data_string
    print("show possible matches")

    #'words.txt'
    #read_file(text)
    smart_list=[ line for line in open('words.txt') if secret_word1 in line]

    #get the value in the list and convert it to a string

    test1=str(smart_list[0])

    #split that string into a list
    temp_list =test1.split()

    #create an empty list to hold the data to be manipulated
    new_list=[]

    #to store the index number

    what_index_is_word=0

    #loop through the
    for index,value in enumerate(temp_list):
        if value==secret_word1:
            #get the index of the word in the list
            what_index_is_word =index
            #check if the index is the begining of the list to avoid index out of range
            if index==0 or index<=10 :
               new_list=temp_list[0:10]
               random.shuffle(new_list)
               print(" ".join(new_list))
            elif index==len(temp_list) or index>=len(temp_list)-10:
                #slice the list and print backing ward
                start=len(temp_list)-10
                end=len(temp_list)
                new_list=temp_list[start:end]
                random.shuffle(new_list)
                print(" ".join(new_list))
            else:
                new_list=temp_list[index-10:index+20]
                random.shuffle(new_list)
                print(" ".join(new_list))
            #print(what_index_is_word)
            break
#===============================================================================
#HANG MAN GAME WITH HINT
#===============================================================================
def hangman_with_hints():
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
     #special string word for pattern matching and comparing  due to lack of time
    special_word=str(secret_word)
    print("special","".join(secret_word))


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

   #vowel words
    vowels_words = ["a","e","i","o","u"]

    #counter to help check if the guess length equal the length of the secret word

    counter = 0

   #start counting the number of loop

    while num_guess > 0 :

        print ("You have",wrong_input_warning,"warnings left.")
        #play the game and also check if it is True
        print("You have", num_guess, "guesses left")

        #show avialable word present
        if num_guess==6:
         print("Available letters: ",string.ascii_lowercase)
        else:
           #print("Available letters: ",get_available_letters(letters_guessed))
           print()
         #a boolean to ensure that if * is enter don't count guess
        is_asterix_enter=False

        #start playing the game
        enter_a_letter = input("Please  guess a letter :  ").lower()

        #letters_guessed = list(input("Please  guess a letter :  "))

        #check if it is a string
        if enter_a_letter.isalpha() and enter_a_letter not in list_to_store_guess_letter or enter_a_letter=="*":

          if enter_a_letter=="*":
            #check if passing the match and also print the guess word

            print("Possible word matches are: ")

            if  match_with_gaps("".join(temp_string),"".join(secret_word)):
                 show_possible_matches("".join(secret_word))

                 is_asterix_enter=True
                #print the avialable word
            else:
                print("False")


          letters_guessed=list(enter_a_letter.lower())

          # add the guess word to the list
          list_to_store_guess_letter.append(enter_a_letter)

        #transverse the list:
          for i in letters_guessed:

             if i in secret_word:
                #start the count

                #letters_guessed.append(users_guess)
                if num_of_time_word_in_scretword==0:

                  temp_string =get_guessed_word(secret_word, letters_guessed)

                  #convert from string to a temporary list to hold the data...

                  data_list1 =list(temp_string.replace(" ", ""))

                  print("Good Guess:",temp_string)

                  data_list2 ="".join(temp_string)

                 # print("testing end game",type(data_list2))

                  num_of_time_word_in_scretword +=1

                  hav_we_enter_loop=True

                  #condition to check if the guess equal the  secret word i.e to end the game

                  if len(data_list2) ==len(secret_word) and '_' not in data_list2:
                        print("Congratulations, you won!")
                      #calculate the game score
                        temp_unique_num=pos_in_secret_word(secret_word,enter_a_letter.lower())

                        number_unique_letters_in_secret_word =temp_unique_num[len(temp_unique_num)-1]

                        total_score = num_guess * number_unique_letters_in_secret_word

                        print("Your total score for this game is: ",total_score)

                        #Terminate the while loop
                        num_guess = -7


                else:
                     for (index,val) in enumerate(secret_word):
                        #if i not in temp_data_list2:
                         if i==val :

                            data_list1[index]=i

                            #crete a second temporary data link list

                            data_list2 = "".join(data_list1)


                            num_of_time_word_in_scretword = 5

                     print("Good Guess:",data_list2)
                     hav_we_enter_loop=True
                      #condition to check if the guess equal the  secret word i.e to end the game

                     display_score_won_game(data_list2,secret_word,num_guess,enter_a_letter)

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

                   if num_of_time_word_in_scretword==0 and is_asterix_enter==False :
                    print("Oops! That letter  is not in my word:",data_list2 )
               # else:
                   if num_guess<4 and is_asterix_enter==False:
                     print("Oops! That letter  is not in my word:",data_list2 )
              else:
                    print("Available letters: ",get_available_letters(letters_guessed))

                    print("Oops! That letter is  not in my word:", data_list2)
              #condition to check if it is vowel word:
              if enter_a_letter in vowels_words:
                  num_guess -=2
                  #print ("VOWEL WORD")
                  if num_guess<=0:
                       print("Sorry, you ran out of guesses. The word was ","".join(secret_word))
              else:
                if is_asterix_enter==False:
                 num_guess -=1

                 if num_guess==0:
                    print("Sorry, you ran out of guesses. The word was ","".join(secret_word))
        else:
            #subtract the warnig  and also check if the warning is zero
            if  wrong_input_warning <=0:
                # reduce the number of guesses
                num_guess -=1
                #check if  the time of guesses is zero and end the game:
                if num_guess==0:
                    print("Sorry, you ran out of guesses. The word was ","".join(secret_word))

            else:
                wrong_input_warning -=1
                if enter_a_letter in list_to_store_guess_letter and hav_we_enter_loop:
                         print ("Oops! You've already guessed that letter. You now have",wrong_input_warning,"warnings left:",data_list2)







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

    # k=list("apple")
    # show_possible_matches("".join(k))
    hangman_with_hints()
    #f=[]
