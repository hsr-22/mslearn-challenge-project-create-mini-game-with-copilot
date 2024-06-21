# create a rock paper scissors game using python

# import random

# def play():
#     user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
#     computer = random.choice(['r', 'p', 's'])

#     if user == computer:
#         return 'It\'s a tie'

#     if is_win(user, computer):
#         return 'You won!'

#     return 'You lost!'

# def is_win(player, opponent):
#     # return true if player wins
#     # r > s, s > p, p > r
#     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
#         return True

# print(play())

import random

# list of options
options = ["r", "p", "s"] # ["rock", "paper", "scissors]

# keep track of score and rounds played
score = 0
rounds = 0

# welcome message
print("Welcome to Rock, Paper, Scissors!")
print("")
# informing the user the available options
print("You can choose from the following options:")
print("r for rock, p for paper, s for scissors")
print("")
# add a note for the user to type in options() if they want to see the options again
print("Type in options() to see the options again")

while True:

    # choose a random option of the list
    computer = random.choice(options)

    # asking for the user input
    player = input("Rock, Paper or Scissors?  ")

    # if player chose rock 
    if player.lower() == "r":
        if computer == "r":
            print("Computer chose rock. It's a tie!")
        elif computer == "p":
            print("Computer chose paper. You lose!")
        elif computer == "s":
            print("Computer chose scissors. You win!")
            score += 1
        rounds += 1

    # if player chose paper
    elif player.lower() == "p":
        if computer == "r":
            print("Computer chose rock. You win!")
            score += 1
        elif computer == "p":
            print("Computer chose paper. It's a tie!")
        elif computer == "s":
            print("Computer chose scissors. You lose!")
        rounds += 1

    # if player chose scissors
    elif player.lower() == "s":
        if computer == "r":
            print("Computer chose rock. You lose!")
        elif computer == "p":
            print("Computer chose paper. You win!")
            score += 1
        elif computer == "s":
            print("Computer chose scissors. It's a tie!")
        rounds += 1

    # if player chose something else
    else:
        print("That's not a valid play. Check your options!")
    
    # if user types in options(), return them the options
    if player == "options()":
        print("You can choose from the following options:")
        print("r for rock, p for paper, s for scissors")

    # ask the user if they want to play again and break the loop if they don't
    # if they break the loop, print the score
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        print(f"You played {rounds} rounds and got {score} points!")
        break