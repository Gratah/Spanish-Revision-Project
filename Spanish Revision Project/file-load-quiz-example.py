import random
import csv
import argparse

def load_list(filename):
    """
    Load data from a CSV file into a list of lists. The format for each entry in the list is itself a 3 item list. This
    program is expecting each row of the input file to contain three elements: index,foreign word,english word.
    These will end up as list items [index,foreign word,english word]

    Parameters:
        filename: Name of CSV file to load. If the file is not in the current folder then the path to the file must be included

    Returns:
        A list of lists of all the rows in the input CSV file: [[index1,foreign word1,english word1],[index2,foreign word2,english word2] etc.
"""
    # Open the file
    with open(filename, 'r', newline='') as f:
        # Use the CSV library to load the file
        reader = csv.reader(f)
        print(type(reader))
        # Return the full list to the caller of the function. The 'list' in this line converts the 'reader' object to a list type
        # using a process called 'casting'. https://www.w3schools.com/python/python_casting.asp
        return(list(reader))
    #endwith
#enddef

def get_words(wordlist, minimum, count):
    """
    Create a selection of items from the full word list based on the number of items required and the minimum length of the foreign word

    Parameters:
        wordlist: A full list of word items from which a sublist is to be selected.
        minimum: The minimum number of letters a word must contain
        count: The number of items to be selected from the full list

    Returns
        The sublist taken from the full list
    """
    # Create the empty list object for the sublist
    selection = []
    # Launch a loop. This loop will continue all the time the length of the sublist (selection) is less that the number of items we want in that list (count)
    while len(selection) < count:
        # Get a random item from the full list
        item = random.choice(wordlist)
        # Check whether the item selected is greater than or equal to the minimum size stated when calling the function.
        # If it is go on to the next line, if not then go round the while loop again
        if len(item[1]) >= minimum:
            # Check that the item randomly chosen was not already randomly chosen. If it is go on to the next line, if not then go round the while loop again
            if item not in selection:
                # Add the selected item to the sublist
                selection.append(item)
            #endif
        #endif
        # Note that the above two 'if' statements could be combined using 'and'. In that case both tests would need to be true before continuing
        # if len(item[1]) >= minimum and item not in selection:
    #endwhile
    # Return the sublist to the caller of the function
    return(selection)
#enddef

def run_quiz(quiz_list):
    """
    Run the quiz by going through each item in the list

    Parametere:
        quiz_list: list of items each containing a list of the format[index,foreign word,english word]

    Return:
        Number of questions that were answered correctly
    """
    score = 0
    # Go through each item in the list
    for turn in quiz_list:
        # Use the index of the items in the list to set to variables. Items in lists always start from 0 so item 0
        # is the first, item 1 is the second etc.
        foreign = turn[1]
        english = turn[2]
        # Prompt for input on the screen. Set whatever is typed in to the variable 'attempt'. This uses '%s' as a placeholder
        # in the input string. This is translated to the value of the variable 'foreign'
        attempt = input("What is the English word for %s?\n" % foreign)
        # Test to see if the attempt matched the English word
        if attempt == english:
            # If it did incrememnt the score
            print("Correct!")
            score = score + 1
        else:
            # If it didn't then show what the correct word is
            print("Incorrect! The English word for '%s' is '%s'\n" % (foreign, english))
        #endif
    #endfor
    # Return the score to the caller of the function
    return(score)
#enddef

def main():
    """
    Argument Parser: This allows you to pass in arguments when you run the script. You can pass in some, all or none of
    these. If the script is just executed on its own then the default values are shown in the declarations.
    Example 1: I want 20 words and them to be a minimum of 5 letters long
        python file-load-quiz-example.py -n 20 -l 5

    Example 2: I want the default values but I want to use a different word list
        python -f wordlist-french.csv

    Note that this is a multi line comment enclosed with triple double quotes. Single line comments start with a #
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--word_list_file", dest="word_file", default="wordlist-full.csv", action="store", type=str,
                        help="Name of CSV file containing the words. Default is 'wordlist-full.csv'")
    parser.add_argument("-l", "--minimum_word_length", dest="minimum", default=4, action="store", type=int,
                        help="The minimum length of the foreign word to be selected. Default is 4.")
    parser.add_argument("-n", "--number of words", dest="word_count", default=10, action="store", type=int,
                        help="Number of words to be selected from the word list. Default = 10.")

    # Translate the parser variables into normal variables. This is not absolutely necesarry but can help with readability
    word_file = parser.parse_args().word_file
    minimum = parser.parse_args().minimum
    word_count = parser.parse_args().word_count

    # Set a variable to what is returned by 'load_list' function. Notice the outcome of the argument parser is being passed as a parameter to the function
    word_list = load_list(word_file)

    # Get a sublist of the full list based on the arguments that I pass into this function call
    quiz_list = get_words(word_list, minimum, word_count)

    # Print that the quiz is starting. Notice that the print statement has placeholders for the word count and minimium
    # length. This time the place holders are '%d' which represents integer types. The '\n' sequence mean newline (for readability)
    print("\nStarting quiz: number of questions = %d, minimum word length = %d\n" % (word_count, minimum))

    # Start the quiz by passing the quiz_list object.
    score = run_quiz(quiz_list)

    # Print the results of the quiz
    print("You scored %d/%d" % (score, word_count))
main()

