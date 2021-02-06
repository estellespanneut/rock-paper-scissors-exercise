# game.py

#need to do: customize player name, check formatting, add comments, make README content
#ATTRIBUTION: while none of my code was taken from other students, all of it was adapted from Professor Rosetti's github, slides, and lectures.



import os
import random

from dotenv import load_dotenv # see: https://github.com/theskumar/python-dotenv

#from app.my_mod import to_usd

#
# 2) After that, we generally run any setup code, like setting environment vars:
#

load_dotenv() # invokes / uses the function we got from the third-party package. this one happens to read env vars from the ".env" file. see the package docs for more info

USER_NAME = os.getenv("USER_NAME", default="Player One") # uses the os module to read the specified environment variable and store it in a corresponding python variable


print("Rock, Paper, Scissors, Shoot!")
print("-------------------")
print("Welcome ", USER_NAME, "to my Rock-Paper-Scissors game...")
print("-------------------")
user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

user_choice.lower()

if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
    print("You Chose: ", user_choice) 
else:
    print("your choice does not match the options")
    quit()



arr = ["rock", "paper", "scissors"]


import random 
computer_choice = random.choice(arr)

print("The computer chose:", computer_choice)


print("-------------------")

if computer_choice == "paper" and user_choice == "scissors":
    print("Congrats! You Won!")
elif computer_choice == "scissors" and user_choice == "rock":
    print("Congrats! You Won!")
elif computer_choice == "rock" and user_choice == "paper":
    print("Congrats! You Won!")
elif computer_choice == user_choice:
    print("It's a tie!")
else:
    print("Oh, the computer won. It's ok.")

print("-------------------")

print("Thanks for playing. Please play again!")

