'''
Name:Aakib Kibria Khan
ID:157802224
email:akkhan9@myseneca.ca


'''




import random

# Create a list of words to choose from
words = ['apple', 'banana', 'cherry', 'grape', 'orange', 'pear', 'strawberry', 'watermelon']

# Choose a random word from the list as the secret word
secret_word = random.choice(words)

# Create a list to store the current state of the word
current_word = ['_'] * len(secret_word)

# Initialize a variable to keep track of the number of incorrect guesses
incorrect_guesses = 0

# Start an infinite loop to play the guessing game
while True:
    # Display the current state of the word with underscores
    print(' '.join(current_word))
    
    # Get a letter guess from the user
    letter_guess = input("Enter your guess: ").lower()

    # Check if the user guessed the entire word correctly
    if letter_guess == secret_word:
        print("You win!")
        break

    # Check if the user guessed a single letter
    if len(letter_guess) == 1 and letter_guess.isalpha():
        # Check if the guessed letter is in the secret word
        if letter_guess in secret_word:
            # Update the current word to reveal the correctly guessed letter(s)
            for i in range(len(secret_word)):
                if secret_word[i] == letter_guess:
                    current_word[i] = letter_guess
        else:
            print("Sorry, my word doesn't contain that letter.")
            incorrect_guesses += 1
    else:
        print("Invalid input. Please guess a letter or the entire word.")

    # Check if the player has guessed the entire word correctly
    if ''.join(current_word) == secret_word:
        print("You win!")
        break

# Display the final word
print("The word was:", secret_word)

    
  