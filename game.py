# game.py in rock-paper-scissors-exercise


#ATTRIBUTION: A large portion of this code was adapted from Professor Rosetti's github, slides, Slack, and lectures.


#import os and random to ensure that the random function works
import os
import random

from dotenv import load_dotenv # see: https://github.com/theskumar/python-dotenv


load_dotenv() # This reads env vars from the ".env" file

USER_NAME = os.getenv("USER_NAME", default="Player One") #stores the env username into a variable, otherwise the value becomes "player one"

#print the opening message once the game starts
print("Rock, Paper, Scissors, Shoot!")
print("-------------------")
print("Welcome '", USER_NAME, "' to my Rock-Paper-Scissors game...")
print("-------------------")
# ask for the user's choice
user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

#turn the user choice into all lowercase letters to reduce the chance of input errors
user_choice.lower() #attribution: this specific code was taken from a student who shared their screen during class. Very helpful!

# data validation to ensure the user chose one of the three valid options
if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
    print("You Chose: ", user_choice) 
else:
    print("your choice does not match the options")
    quit() #if something other than rock, paper, or scissors is chosen, the game displays an error message and ends


# create a list / array variable with the three game options 
arr = ["rock", "paper", "scissors"]

#computer choice is selected randomly from the list created 
computer_choice = random.choice(arr)

#print the computer's choice
print("The computer chose:", computer_choice)


print("-------------------")


#calcultate and display if the user won, if the computer won, or if it was a tie
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

#game ends