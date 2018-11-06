# -*- coding: utf-8 -*-
#Hangman game - A secret word is given and the user tries to find it

#When user loses, print the proper message (and the hanged man!)
def game_over():
    print("\t  @@@@@@@@@@@@   \n\t  ....,@@,,..@   \n\t        @@   @   \n\t         @@  @   \n\t          @@ @   \n\t  @@       @@@   \n\t .@@#       @@   \n\t  ,@@@       @   \n\t  @@@@       @   \n\t `@@@@:      @   \n\t '+@@;#      @   \n\t .'@@ ,      @   \n\t   @@       :@   \n\t   @@       @@;  \n\t   @@       @@@  \n\t   @@      @`@@; \n\t           @ @ @ \n")
    print("\nYou have been hanged..\n")

#Replaces the solution list with the known letters
def print_known(word, letter, output, flag):
    counts = 0
    for i in word:
        if letter == i:
            output[counts] = letter
        counts = counts + 1
    if word == ''.join(output):
        flag = 1
    return output, flag

#Checks if letter given by user exists in the word
def check_letter(word, letter):
    times = 0
    for character in word:
        if letter == character:
            times = times + 1
    return times

print("\n|---------------------------|")
print("| Welcome to Hang-man game! |")
print("|---------------------------|\n")

secret_list = ["programing", "kernel", "nihao"]
hint_list = ["The purpose of life", "If you go to close you will get burned", "Chinese hello!"]
solution = list()
success = 0
total_games = 0

for wd, hint in zip(secret_list, hint_list):

    ans = input("Do you wanna play (y/n)?  ")
    ans = ans.lower()

    while (ans != 'y' and ans != 'n'):
        ans = input("Do you wanna play (y/n)?   ")
        ans = ans.lower()

    if (ans == 'y'):
        total_games = total_games + 1
        total_lifes = len(wd)
        print("Find the {} letters below:".format(len(wd)))
        print("\tHint: {} \n".format(hint))
        solution = list("-")*len(wd)
        print(''.join(solution))
        found = 0

        while (total_lifes > 0 and found == 0):

            #Not case sensitive
            ans = input("Enter a letter: ")
            ans = ans.lower()

            counter = check_letter(wd, ans)

            if counter == 0:
                print("Letter not found")
                total_lifes = total_lifes - 1
                print("You have {} lifes left".format(total_lifes))
            else:
                print("{} Letter(s) found!".format(counter))

            solution, found = print_known(wd, ans, solution, found)
            print(''.join(solution))

        if found:
            print("\nCongratulations!\n\n")
            success = success + 1
        else:
            game_over()
            print("The word was '{}'\n\n".format(wd))

    else:
        break

if total_games > 0:
    print("You had a {0:3.2f}% success rate!".format(100*(success/total_games)))
else:
    print("No statistic data")