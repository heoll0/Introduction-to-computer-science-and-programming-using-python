# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
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


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    a=len(secret_word)
    b=len(letters_guessed)
    c=0
    for i in range(a):
        for j in range(b):
            if secret_word[i]==letters_guessed[j]:
                c=c+1
    if c==a:
        boolean = True
    else:
        boolean = False
    return boolean


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed=''
    a=len(secret_word)
    b=len(letters_guessed)
    for i in range(a):
        c=False
        for j in range(b):
            if secret_word[i]==letters_guessed[j]:
                guessed=guessed+secret_word[i]
                c=True
        if not c:
            guessed=guessed+'_'+' '
    return guessed




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    b=len(letters_guessed)
    guessed=''
    for i in range(26):
        c=False
        for j in range(b):
            if string.ascii_lowercase[i]==letters_guessed[j]:
                c=True
        if not c:
            guessed=guessed+string.ascii_lowercase[i]
    return guessed
    
    

def hangman(secret_word):
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game hangman!')
    print('I am thinking a word that is',len(secret_word),'letters long')
    print('You have 3 warnings left')
    print('--------------------------------------')
    letters_guessed=[]  
    uniqueLettersIn_secret_word=0
    guesses_remaining=6
    warnings_remainings=3           
    while guesses_remaining>0 and not is_word_guessed(secret_word, letters_guessed):
            print('You have',guesses_remaining,'guesses left')
            print('Available letters:',get_available_letters(letters_guessed))
            print('abc')
            a=input('Please guess a letter:')
            d=True
            for x in range(len(letters_guessed)):
                if a==letters_guessed[x]:
                    d=False
            if str.isalpha(a) and d:
                a=str.lower(a)
                letters_guessed.append(a)
                c=False
                for j in range(len(secret_word)):
                    if secret_word[j]==a:
                       c=True
                if c:
                    uniqueLettersIn_secret_word+=1
                    print('Good guess:',get_guessed_word(secret_word, letters_guessed))            
                else:
                    print('Oops,That letter is not in my word:',get_guessed_word(secret_word, letters_guessed))
                    if a=='a'or a=='e' or a=='i' or a=='o':
                        guesses_remaining-=2
                    else:
                        guesses_remaining-=1      
            else:
               warnings_remainings-=1
               if warnings_remainings<0:
                   print('You have no warnings left')
                   print('So you lose one guess:',get_guessed_word(secret_word, letters_guessed))
                   guesses_remaining-=1
               elif not d:
                   print('Oops!You have already guesses that letter.You have',warnings_remainings,'warnings left:')
                   print(get_guessed_word(secret_word, letters_guessed))
               else:
                   print('Oops!That is not a valid letter.You have',warnings_remainings,'warnings left:',get_guessed_word(secret_word, letters_guessed))  
            print('--------------------------------------')
    if is_word_guessed(secret_word, letters_guessed):      
        print('Congratulations!You won')
        print('Your total score for this game is:',guesses_remaining*uniqueLettersIn_secret_word)
    else:
        print('Sorry,you ran out of guesses.The word was:',secret_word)
                 
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    a=0
    b=True
    i=0
    boolean=False
    _number=0
    letters_number=0
    letters_location=[]
    myletters_location=[]
    _location=[]
    while i < len(my_word):
        if str.isalpha(my_word[i]):
            letters_number+=1
            letters_location.append(i-_number)
            myletters_location.append(i)
            i=i+1
        else:
            _location.append(i-_number)
            _number+=1
            i=i+2
    word_len=int((len(my_word)-letters_number)/2+letters_number)
    if word_len==len(other_word):
        for j in range(len(letters_location)):
            if my_word[myletters_location[j]]==other_word[letters_location[j]]:
                a=a+1
            for k in range(len(_location)):
                if other_word[letters_location[j]]==other_word[_location[k]]:
                    b=False
        if b and a==len(letters_location):
            boolean=True
        else:
            boolean=False
    return boolean



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    match_my_word=''
    boolean=False
    for i in range(len(wordlist)):
        if match_with_gaps(my_word,wordlist[i]):
            match_my_word=match_my_word+wordlist[i]+' '
            boolean=True
    if boolean:
        print(match_my_word)
    else:
        print('No matches found')
    



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    print('Welcome to the game hangman!')
    print('I am thinking a word that is',len(secret_word),'letters long')
    print('You have 3 warnings left')
    print('--------------------------------------')
    letters_guessed=[]  
    uniqueLettersIn_secret_word=0
    guesses_remaining=6
    warnings_remainings=3           
    while guesses_remaining>0 and not is_word_guessed(secret_word, letters_guessed):
            print('You have',guesses_remaining,'guesses left')
            print('Available letters:',get_available_letters(letters_guessed))
            a=input('Please guess a letter:')
            if a=='*':
                print('Possible word matches are:')
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            else:
                d=True
                for x in range(len(letters_guessed)):
                    if a==letters_guessed[x]:
                        d=False
                if str.isalpha(a) and d:
                    a=str.lower(a)
                    letters_guessed.append(a)
                    c=False
                    for j in range(len(secret_word)):
                        if secret_word[j]==a:
                           c=True
                    if c:
                        uniqueLettersIn_secret_word+=1
                        print('Good guess:',get_guessed_word(secret_word, letters_guessed))            
                    else:
                        print('Oops,That letter is not in my word:',get_guessed_word(secret_word, letters_guessed))
                        if a=='a'or a=='e' or a=='i' or a=='o':
                            guesses_remaining-=2
                        else:
                            guesses_remaining-=1      
                else:
                   warnings_remainings-=1
                   if warnings_remainings<0:
                       print('You have no warnings left')
                       print('So you lose one guess:',get_guessed_word(secret_word, letters_guessed))
                       guesses_remaining-=1
                   elif not d:
                       print('Oops!You have already guesses that letter.You have',warnings_remainings,'warnings left:')
                       print(get_guessed_word(secret_word, letters_guessed))
                   else:
                       print('Oops!That is not a valid letter.You have',warnings_remainings,'warnings left:',get_guessed_word(secret_word, letters_guessed))  
            print('--------------------------------------')
    if is_word_guessed(secret_word, letters_guessed):      
        print('Congratulations!You won')
        print('Your total score for this game is:',guesses_remaining*uniqueLettersIn_secret_word)
    else:
        print('Sorry,you ran out of guesses.The word was:',secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #secret_word = 'apple'
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
