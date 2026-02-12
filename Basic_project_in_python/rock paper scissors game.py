
# Rock, Paper ,Scissors game:
#import required module
import random

# Define options for the game
option = ("rock" ,"paper" ,"scissors")

running = True  # Control variable to run the game loop

while running: # Game loop runs until the user decides to stop playing
    # Initialize player choice to None and randomly select computer choice
    player = None
    computer = random.choice(option)
    while player not in option :
        player=input("Enter a choice (rock / paper / scissors ) : ").lower()

    print()
    print(f"player : {player}")  # print player and computer choices
    print(f"computer : {computer}") # print player and computer choices

    # Determine the winner based on the rules of the game
    if player == computer :
        print("It's Tie!")
    elif player == "rock" and computer== "scissors":
        print("You win!")
    elif player == "paper" and computer== "rock":
        print("You win!")
    elif player == "scissors" and computer== "paper":
        print("You win!")
    else:
        print("You lose!")
    print()
    # Ask the user if they want to play again
    play_again = input("Play again? (Y/N) : ") .lower()
    if not play_again == "y":  # if user does not want to play again, stop the game loop
       running = False # Stop the game loop
# After the game loop ends, print a thank you message
print("Thanks for playing!")