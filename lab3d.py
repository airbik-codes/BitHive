
'''
Name: Aakib Kibria Khan
Student_ID: 157802224
'''


# Import the 'random' module to generate a random number.
import random

# Generate a random secret number between 1 and 10 (inclusive).
secret = random.randint(1, 10)

# Initialize a variable 'user_input' with an initial value of 0.
user_input = 0




# Start a loop that continues until the user correctly guesses the secret number (7).
while user_input != 7:
    # Prompt the user to guess a number between 1 and 10.
    user_input = int(input("Guess a number between 1 and 10: "))
    
    # Check if the user's guess is not equal to the secret number.
    if user_input != secret:
        # If the guess is incorrect, inform the user.
        print("Sorry, that's not it.")
    else:
        # If the guess is correct (equal to the secret number), inform the user that they win.
        print("Correct! You win.")
