# rock-paper-scissors-exercise


## Requirements

  + Python 3.7+
  + Anaconda 3.7+
  + Pip
  + VSCode or similar software (editors will be referred to simply as 'VSCode')
  + GitBash or another command line software (will simply be referred to as GitBash or the command line)

## Game Overview 

This "Rock, Paper, Scissors" game is an interactive game using the command line. This game follows the traditional rules of Rock, Paper, Scissors, played against the computer. For a refresher on the rules of Rock, Paper, Scissors, please visit https://www.wrpsa.com/the-official-rules-of-rock-paper-scissors/


## Setup

Using this online Github repository, click "Fork" to copy this game repository into your personal Github. Using GitHub Desktop, clone this version onto your desktop. 

Use the command-line to navigate into the local repository.
```sh
cd ~/Desktop/rock-paper-scissors-exercise
```

Use Anaconda to create and activate a new virtual environment, perhaps called "my-game-env":

```sh
conda create -n my-game-env python=3.8 # (first time only)
conda activate my-game-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```
---

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username:

    USER_NAME="John Snow" #Replace the name inside the quotation marks with your own name or whatever you want displayed as your username for the game

Alternatively, once you have created the .env file, you can configure your username in the command line by typing the code below. This is simply an alterative to configuring your .env file through VSCode, and should not be done in addition to the step above.  

    USER_NAME="Jane" python my_game.py #Replace the name inside the quotation marks with your own name or whatever you want displayed as your username for the game



## Game Instructions 

Once you have completed the setup section above, you are ready to play the game. 

Make sure that you are still in the game's directory in the command line. You can then access the game by typing the following into your command line:

```sh
python game.py
```

The following message should be displayed, perhaps with a different username displayed based on what you configured earlier:

```
-------------------
Welcome 'Player One' to my Rock-Paper-Scissors game...
-------------------
Please choose either 'rock', 'paper', or 'scissors': 
```

Once you see this message, choose between rock, paper, and scissors. Type this selection into the command line and press enter. Note that if you make a typo or choose anything else, GitBash will send you an error message and the game will stop.

Once you have selected your choice, the computer will randomly choose between rock, paper, and scissors, and the outcome will be presented to you in a message similar to this one:

```
-------------------
Welcome 'Player One' to my Rock-Paper-Scissors game...
-------------------
Please choose either 'rock', 'paper', or 'scissors': rock
You chose: 'rock'
The computer chose: 'paper'
-------------------
Oh, the computer won. It's ok.
-------------------
Thanks for playing. Please play again!
```

At this point, the game is over. You can restart the game by following the steps in this "Game Instructions" section again. 

