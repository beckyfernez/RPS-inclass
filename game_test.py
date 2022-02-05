


# This is the "game_test.py" file...
#
# FYI: this is to satisfy the OPTIONAL testing challenge objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/challenges.md
#

from game import determine_winner


def test_determine_winner():

    assert determine_winner("Rock", "Rock") == None # represents a tie
    assert determine_winner("Rock", "Paper") == "Paper"
    assert determine_winner("Rock", "Scissors") == "Rock"

    assert determine_winner("Paper", "Rock") == "Paper"
    assert determine_winner("Paper", "Paper") == None # represents a tie
    assert determine_winner("Paper", "Scissors") == "Scissors"

    assert determine_winner("Scissors", "Rock") == "Rock"
    assert determine_winner("Scissors", "Paper") == "Scissors"
    assert determine_winner("Scissors", "Scissors") == None # represents a tie
