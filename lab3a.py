'''
Name: Aakib Kibria Khan
Student_ID: 157802224
'''

# Initialize variables to keep track of the current question number and the player's score.
num = 0
score = 0

# Start a loop that continues until the current question number is 26.
while num != 26:
    # Prompt the user to enter the answer to 12+14 or press 's' to skip.
    user_input = input("Enter the answer to 12+14, or press 's' to skip: ")
    
    # Check if the user input is 's' (skip).
    if user_input == 's':
        # If 's' is pressed, inform the user that the question is skipped and award 0 points.
        print("Question skipped. 0 points awarded.")
        # Exit the loop using the break statement.
        break
    else:
        # Convert the user input to an integer.
        num = int(user_input)
        if num != 26:
            # If the user's answer is incorrect, inform them and allow them to try again.
            print("Incorrect. Try again.")
        else:
            # If the user's answer is correct, inform them and award 1 point.
            print("Correct! You have been awarded 1 point!")
            # Increment the player's score.
            score += 1

# Inform the user that the next question is about to begin.
print("Next Question...")

# Repeat the above process for the next three questions (23+8, 30+13, and 17+27) with their respective numbers and messages.
# Each time, the user has the option to skip the question by pressing 's'.
# The user's score is updated accordingly.

# Calculate the player's final grade as a percentage (percentage of correct answers out of 4).
grade = (score / 4) * 100

# Display the player's final grade.
print("You received a grade of " + str(round(grade, 1)) + "%.")
