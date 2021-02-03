# game.py

print("Rock, Paper, Scissors, Shoot!")
print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")
x = input("Please choose either 'rock', 'paper', or 'scissors': ")


if x == "rock" or "paper" or "scissors":
    print("You Chose: ", x) 
else:
    print("your choice does not match the options")
    quit()

arr = ["rock", "paper", "scissors"]
# import random 
# random.choice(arr)

# print("the computer chose:", random)


print("-------------------")

print("Oh, the computer won. It's ok.")

print("-------------------")

print("Thanks for playing. Please play again!")

