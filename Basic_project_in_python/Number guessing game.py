
# Create a number gussing game :

## Import required module
import random

# Set the range for the number
low=1
high=100

# Generate a random number between low and high
number=random.randint(low,high)

# Variable to count number of attempts
guesses= 0

is_running = True   # Control variable to run the game loop
print()
print("-----Wel-Come to the number gussing game-----")
print(f"Select a number between {low} and {high}")


# Game loop runs until the correct number is guessed
while is_running:
    guess=input("Enter your gusses : ")

    # Check if input is a valid number
    if guess.isdigit():
     guess=int(guess)
     guesses+=1

   # Check if the guess is within the valid range
     if guess < low or guess > high:
       print("That number out of range.")
       print(f"Please Select a number between {low} and {high} ")
     elif guess < number:
        print("Select higher number! Try again")
        print()
     elif guess > number:
        print("Select lower number! Try again")
        print()
        
     else:
        # If guess is correct
        print("\n\n------------RESULT ------------")
        print(f"CORRECT! The answer is {number}")
        print(f"Number of guesses : {guesses}")
        print("-------------------------------")
        is_running = False   # Stop the game loop
    else:
      # If user enters non-numeric value
     print("Invalid guesses")
     print(f"Please Select a number between {low} and {high} ")


