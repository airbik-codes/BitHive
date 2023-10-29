'''
Name: Aakib Kibria Khan
Student_ID: 157802224
'''
import random

# Generate a random number between 1 and 10 and store it as 'secret'
secret = random.randint(1, 10)

# Initialize 'user_input' to 0 to enter the loop
user_input = 0

# Continue looping until 'user_input' matches the 'secret' number
while user_input != secret:
    # Prompt the user to guess a number between 1 and 10
    user_input = input("Guess a number between 1 and 10: ")

    # Check if the user's input is a numeric value
    if user_input.isnumeric():
        # Convert the user's input to an integer
        user_input = int(user_input)

        # Check if the user's input is within the valid range (1 to 10)
        if 1 <= user_input <= 10:
            # Check if the user's input matches the 'secret' number
            if user_input != secret:
                print("Sorry, that's not it.")
            else:
                print("Correct! You win.")
        else:
            # If the input is out of bounds, print an error message
            print("Error: not a number or out of bounds.")
    else:
        # If the input is not a number, print an error message
        print("Error: not a number or out of bounds.")


        
        
        
        
       
