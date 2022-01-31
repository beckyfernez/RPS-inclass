
#  Write Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md



# this is the "game.py" file
print ("Rock, Paper, Scissors, Shoot!")


#ASK FOR USER INPUT
userChoice = input("Please choose either : 'Rock', 'Paper', or 'Scissors': ")
print ("You chose : ", userChoice)
    #eventually I want to convert all variations of "ROCK" into the standard "Rock"


#VALIDATE USER INPUT
if userChoice == "Rock":
    print ("You chose : ", userChoice)
else:
    print("Sorry that is not a valid input. You have exited the game.")
    quit()


#COMPUTER CHOICE (Generating a computer selection)
#Use a library of python code - "module"
#https://docs.python.org/3/library/random.html#random.choice
# https://www.geeksforgeeks.org/python-select-random-value-from-a-list/
# https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/modules/random.md

import random
gameOptions = ['Rock', 'Paper', 'Scissors']
comChoice = random.choice(gameOptions)
print("The computer chose : ", comChoice)

#alternative way to import random function from library module
#from random import choice
#comChoice = choice(gameOptions)


#DETERMINE WINNER
#when to use elif and its syntax
if userChoice == comChoice:
    print ("We have a tie.")
if userChoice == "Rock" and comChoice == "Paper":
    print ("Oh, the computer won. It's okay.")
if userChoice == "Rock" and comChoice == "Scissors":
    print ("You won!")


#RETURN FINAL RESULTS


#Ask if user would like to play again
replay = input("Would you like to play again? Choose 'Yes' or 'No' : ")
if replay == "No":
    quit()
if replay == "Yes":