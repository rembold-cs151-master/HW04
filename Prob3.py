##################################################
# Name:
# Collaborators:
##################################################



def load_words():
    """ 
    This function loads all the words in 'words.txt'
    into a list that can then be randomly chosen from.
    You don't need to touch this function, as it is all
    setup for you, and we haven't talked about reading
    or writing to files yet.
    """
    with open('words.txt', 'r') as f:
        line = f.readline()
    wordlist = line.split()
    print(" --- ", len(wordlist), "words loaded. --- ")
    print("")
    return wordlist


def get_random_word():
    """
    Function which uses 'load_words()' to grab the
    full list of words from the text document and
    then randomly chooses one to be returned.

    You do not need to edit anything in this function.
    """
    import random
    wordlist = load_words()
    return random.choice(wordlist)


def generate_status(word, letters_guessed):
    """
    Function to return a string of the form
    __a_rt where correctly guessed letters
    have been filled in.

    Takes two inputs:
     - word (string): 
            the actual word the user is trying to guess.
     - letters_guessed (string):
            a string of all the guessed letters

    Output should be a string the same length as word
    but with any unguessed letters replaced by underscores.
    """
    pass #<--- remove this once you actually add your code below


def remaining_guesses(curr_rem_guesses, letter_guessed, word):
    """
    Each time a guess is made the program needs to determine
    if it should add 1 to the incorrect guesses score. This function
    makes the necessary checks and then returns the new number of
    remaining guesses.

    Takes 3 inputs:
     - curr_rem_guesses (int):
            The current number of remaining guesses (before latest guess)
     - letter_guessed (string):
            What letter was guessed by the user
     - word (string):
            The actual word the user is trying to guess

    Should output a single value of integer form, which is the remaining
    number of incorrect guesses the player has available.
    """
    pass #<--- remove this once you actually add your code below



def play(word = get_random_word()):
    """
    This is the main function to play the actual game.

    One optional input:
     - word (string):
        Any word to be guessed can be passed to this function. If no word is
        passed, then the program will randomly select one from the list of
        words loaded in earlier.

    One output:
     - (string)
        Program should return 'Win' if the player wins or 'Lose' if the player
        loses.
    """
    # Initialize variables

    # Main program loop to ask for input and display output until win or lose





    # After loop ends print statements

    # And don't forget to return something!


# The below code just serves to only run your program if it is run directly,
# that is, if it is not imported by some other program. It is a good practice,
# and one that you should keep as it is what lets the auto-tests run nicely.
if __name__ == '__main__':
    # If you want to test your program with a specific word, you can enter
    # it in as play(your word) below. But maybe sure nothing is there (so
    # it defaults to a random word) when you actually submit it!
    play()
