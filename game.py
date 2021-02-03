# game.py

print("Rock, Paper, Scissors, Shoot!")
print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")
user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")


if user_choice == "rock" or "paper" or "scissors":
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

