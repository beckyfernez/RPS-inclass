
#     Write Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md


#  This is the "game.py" file


#https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/modules/os.md#Environment-Variables
import os
player_name = os.getenv("PLAYER_NAME", default="Player One")


#https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/challenges.md
def determine_winner(choice_1, choice_2):
    """
    Determines the winning choice between two valid choices from selectable options: "Rock", "Paper", or "Scissors".
    Returns the winning choice (e.g. "Paper"), or None if there is a tie.
    Example: determine_winner("Rock", "Paper")
    """
    if choice_1 == choice_2:
        return "None"
    if choice_1 == "Rock":
        if choice_2 == "Paper":
            return "Paper"
        if choice_2 == "Scissors":
            return "Rock"
    if choice_1 == "Paper":
        if choice_2 == "Rock":
            return "Paper"
        if choice_2 == "Scissors":
            return "Scissors"
    if choice_1 == "Scissors":
        if choice_2 == "Rock":
            return "Rock"
        if choice_2 == "Paper":
            return "Scissors"


print("-------------------")
print(" ")
print("Welcome '", player_name, "' to my game...")
print("Rock, Paper, Scissors, Shoot!")
print(" ")
print("-------------------")
print(" ")


#  ASK FOR USER INPUT
#use pyhton function title() to convert any capitalization of each choice into proper case
#https://www.datasciencemadesimple.com/lower-upper-title-function-python/#:~:text=title()%20Function%20in%20python,and%20the%20rest%20are%20lowercase.
#https://stackoverflow.com/questions/8772142/converting-to-upper-case-which-way-is-more-pythonic
userChoice = input("Please choose either : 'Rock', 'Paper', or 'Scissors': ")
userChoice = userChoice.title()


#  VALIDATE USER INPUT
#adapted from a class lesson in the course "Decision Support Systems"
if userChoice == "Rock" or userChoice == "Paper" or userChoice == "Scissors":
    print("You chose :", userChoice)
else:
    print(" ")
    print("Oops, that is not a valid input. The game has exited.")
    quit()


#  COMPUTER CHOICE (Generating a computer selection)
#Use a library of python code - "module"
#https://docs.python.org/3/library/random.html#random.choice
#https://www.geeksforgeeks.org/python-select-random-value-from-a-list/
#https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/modules/random.md
import random
gameOptions = ['Rock', 'Paper', 'Scissors']
comChoice = random.choice(gameOptions)
print("The computer chose :", comChoice)
#alternative way to import random function from library module
#from random import choice
#comChoice = choice(gameOptions)


#  DETERMINE WINNER
#This section of code was adapted from class lecture and slack comments
#I originally was doing compound if statements but instead chose to go with nested if statements
if userChoice == comChoice:
    print("We have a tie.")
elif userChoice == "Rock":
    if comChoice == "Paper":
        print("Oh, the computer won. It's okay.")
    else:
        print("You won!")
elif userChoice == "Paper":
    if comChoice == "Rock":
        print("You won!")
    else:
        print("Oh, the computer won. It's okay.")
print(" ")
print("Thanks for playing. Please play again!")