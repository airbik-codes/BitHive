'''
Name: Aakib Kibria Khan
Student_ID: 157802224
'''

# Import the 'random' module to generate random numbers.
import random

# Initialize variables to keep track of the question number and the player's score.
question_number = 0
score = 0

# Start an infinite loop to keep asking questions until the user decides to quit.
while True:
    # Generate two random numbers between 1 and 10.
    secret_number1 = random.randint(1, 10)
    secret_number2 = random.randint(1, 10)
    
    # Calculate the correct answer to the question.
    secret = secret_number1 + secret_number2
    
    # Increment the question number.
    question_number += 1
    
    # Prompt the user to enter their answer or take other actions.
    user_input = input("Enter the answer to " + str(secret_number1) + " + " + str(secret_number2) + ", Press 's' to skip or 'q' to quit: ")
    
    # Check if the user wants to quit the quiz.
    if user_input == 'q':
        break
    elif user_input == 's':
        # If the user wants to skip the question, inform them and award 0 points.
        print("Question skipped. 0 points awarded.")
        continue
    else:
        # Convert the user's input to an integer.
        user_input = int(user_input)
        
        # Check if the user's answer is correct.
        if user_input != secret:
            # If the answer is incorrect, inform the user.
            print("Incorrect. Try again.")
        else:
            # If the answer is correct, inform the user, award 1 point, and move to the next question.
            print("Correct! You have been awarded 1 point!")
            score += 1
            print("Next question...")

# Calculate the player's final score as a percentage of correct answers out of the total questions.
result = (score / (question_number - 1)) * 100

# Display the quiz results, including the final score as a percentage.
print("Quiz over. You scored " + str(round(result, 1)) + "%.")



        




