# -*- coding: utf-8 -*-

"""Hangman game - A secret word is given and the user tries to find it"""

def game_over():
    """When user loses, print the proper message (and the hanged man!)"""
    print("\t  @@@@@@@@@@@@   \n\t  ....,@@,,..@   \n\t",
          "        @@   @   \n\t         @@  @   \n\t",
          "          @@ @   \n\t  @@       @@@   \n\t .@@#",
          "       @@   \n\t  ,@@@       @   \n\t",
          "  @@@@       @   \n\t `@@@@:      @   \n\t",
          " '+@@;#      @   \n\t .'@@ ,      @   \n\t",
          "   @@       :@   \n\t   @@       @@;  \n\t",
          "   @@       @@@  \n\t   @@      @`@@; \n\t",
          "           @ @ @ \n")
    print("\nYou have been hanged..\n")

def print_known(word, letter, output, flag):
    """Replaces the solution list with the known letters"""
    counts = 0
    for i in word:
        if letter == i:
            output[counts] = letter
        counts = counts + 1
    if word == ''.join(output):
        flag = 1
    return output, flag

def check_letter(word, letter):
    """Checks if letter given by user exists in the word"""
    times = 0
    for character in word:
        if letter == character:
            times = times + 1
    return times

# Welcome message
print("\n|---------------------------|")
print("| Welcome to Hang-man game! |")
print("|---------------------------|\n")

# List of words to be found
SECRET_LIST = ["programming", "kernel", "nihao"]
# List of hints to the corresponding words
HINT_LIST = ["The purpose of life", "If you go to close you will get burned", "Chinese hello!"]
SOLUTION = list()
# Statistics
SUCCESS = 0
TOTAL_GAMES = 0

for wd, hint in zip(SECRET_LIST, HINT_LIST):

    ans = input("Do you wanna play (y/n)?  ")
    ans = ans.lower()

    # Validation check for ans
    while ans not in ('y', 'n'):
        ans = input("Do you wanna play (y/n)?   ")
        ans = ans.lower()

    if ans == 'y':
        TOTAL_GAMES = TOTAL_GAMES + 1
        total_lifes = len(wd)
        print("Find the {} letters below:".format(len(wd)))
        print("\tHint: {} \n".format(hint))
        SOLUTION = list("-")*len(wd)
        print(''.join(SOLUTION))
        found = 0

        while (total_lifes > 0 and found == 0):

            # Not case sensitive
            ans = input("Enter a letter: ")
            ans = ans.lower()

            # Check if ans is just a letter and not a word or a number
            while (len(ans) != 1) or ans.isdigit():
                ans = input("Enter a letter: ")
                ans = ans.lower()

            # Count the times that the letter is found in the word
            counter = check_letter(wd, ans)

            # And print the proper message
            if counter == 0:
                print("Letter not found")
                total_lifes = total_lifes - 1
                print("You have {} lifes left".format(total_lifes))
            else:
                print("{} Letter(s) found!".format(counter))

            # Print the found letters of the word with the right function
            SOLUTION, found = print_known(wd, ans, SOLUTION, found)
            print(''.join(SOLUTION))

        if found:
            print("\nCongratulations!\n\n")
            SUCCESS = SUCCESS + 1
        else:
            game_over()
            print("The word was '{}'\n\n".format(wd))

    else:
        break

# Collect and display some statistic data
if TOTAL_GAMES > 0:
    print("You had a {0:3.2f}% success rate!".format(100*(SUCCESS/TOTAL_GAMES)))
else:
    print("No statistic data")
