# Rock Paper Scissors-game

A Completed Repository for the [Rock Paper Scissors Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md).

Some descriptions have been adapted from the tic-tac-toe repository belonging to Professor Rossetti.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Setup

Optionally fork this [remote repository](https://github.com/beckyfernez/RPS-inclass), to create a copy under your own control. Then "clone" or download the remote repository (or your forked copy) onto your local computer, for example to your Desktop. Then navigate to wherever you downloaded the repo:

```sh
cd ~/Desktop/RPS-inclass
```

Create a virtual environment:

```sh
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```sh
conda activate rps-env
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```

## Player Types

When playing the game:

player type(s) | description
--- | ---
`HUMAN` | A human player who will input their selections.
`COMPUTER` | A computer player which makes a random selection.

## Usage

Configure your own player name and run the rock paper scissors game (human vs computer):

```sh
PLAYER_NAME="Jon Snow" python game.py
```

OR

Continue with default name, 'Player One', and Run the rock paper scissors game (human vs computer):

```sh
python game.py
```

The game will only run once.

## Testing

Run tests:

```sh
pytest
```

## Demo

Here is a demonstration of gameplay:

```
-------------------

Welcome 'Player One' to my game...
Rock, Paper, Scissors, Shoot!

-------------------

Please choose either : 'Rock', 'Paper', or 'Scissors': Rock
You chose :  Rock
The computer chose :  Scissors
You won!

Thanks for playing. Please play again!
```