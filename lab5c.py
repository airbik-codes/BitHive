'''
Name:Aakib Kibria Khan
ID:157802224
email:akkhan9@myseneca.ca


'''




import random

# Create a list of animal names
animals = ['snake', 'hamster', 'scorpion', 'beaver', 'mosquito', 'camel', 'vulture', 'horse', 'python', 'capybara']

# Choose a random animal name from the list as the secret word
secret = animals[random.randint(0, len(animals) - 1)]

# Start an infinite loop to play the guessing game
while True:
    # Display a message to inform the user of the game
    print("I'm thinking of an animal. Can you guess what it is?")
    
    # Get user input for a letter or a guess, or press Enter to quit
    user_guess = input("Enter a letter or a guess. Press enter to quit: ")

    # Check if the user pressed Enter to quit the game
    if user_guess == "":
        break
    # Check if the user's guess matches the secret word
    elif user_guess == secret:
        print("You win!")
        break
    # Check if the user's input is a single letter and is alphabetic
    elif len(user_guess) == 1 and user_guess.isalpha():
        # Check if the guessed letter is in the secret word
        if user_guess in secret:
            print("Yes, my word contains that letter.")
        else:
            print("Sorry, my word doesn't contain that letter.")
    else:
        # Inform the user that their input is not valid
        print("Sorry, that's not it.")

    
  