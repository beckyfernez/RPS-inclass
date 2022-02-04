
#   To do: Write Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md



#  This is the "game.py" file
print ("Rock, Paper, Scissors, Shoot!")



#  ASK FOR USER INPUT
#use pyhton function title() to convert any capitalization of each choice into proper case
#https://www.datasciencemadesimple.com/lower-upper-title-function-python/#:~:text=title()%20Function%20in%20python,and%20the%20rest%20are%20lowercase.
#https://stackoverflow.com/questions/8772142/converting-to-upper-case-which-way-is-more-pythonic
userChoice = input("Please choose either : 'Rock', 'Paper', or 'Scissors': ")
userChoice = userChoice.title()



#  VALIDATE USER INPUT
#adapted from a class lesson in the course "Decision Support Systems"
if userChoice == "Rock" or userChoice == "Paper" or userChoice == "Scissors":
    print ("You chose : ", userChoice)
else:
    print("Sorry that is not a valid input. You have exited the game.")
    quit()



#  COMPUTER CHOICE (Generating a computer selection)
#Use a library of python code - "module"
#https://docs.python.org/3/library/random.html#random.choice
#https://www.geeksforgeeks.org/python-select-random-value-from-a-list/
#https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/modules/random.md

import random
gameOptions = ['Rock', 'Paper', 'Scissors']
comChoice = random.choice(gameOptions)
print("The computer chose : ", comChoice)

#alternative way to import random function from library module
#from random import choice
#comChoice = choice(gameOptions)



#  DETERMINE WINNER
#This section of code was adapted from class lecture and slack comments
#I originally was doing compound if statements but instead chose to go with nested if statements
if userChoice == comChoice:
    print ("We have a tie.")
elif userChoice == "Rock":
    if comChoice == "Paper":
        print ("Oh, the computer won. It's okay.")
    else:
        print ("You won!")
elif userChoice == "Paper":
    if comChoice == "Rock":
        print ("You won!")
    else:
        print ("Oh, the computer won. It's okay.")



#RETURN FINAL RESULTS


#Ask if user if they would like to play again

#replay = input("Would you like to play again? Choose 'Yes' or 'No' : ")
#if replay == "No":
#    quit()
#if replay == "Yes":

#maybe a GoTo statement


