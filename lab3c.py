'''
Name: Aakib Kibria Khan
Student_ID: 157802224
'''


# Initialize a variable 'sum' with an initial value of 0 to keep track of the sum.
sum = 0

# Print a header message to indicate the purpose of the program.
print("SUMMING CALCULATOR")

# Start an infinite loop that continues until explicitly terminated by the user.
while True:
    # Display the current sum to the user.
    print("The sum so far: " + str(sum))
    
    # Prompt the user to enter a number to add to the sum or press Enter to exit the program.
    user_input = input("Enter a number to add to your sum. Pressing enter will exit. ")
    
    # Check if the user pressed Enter (empty input).
    if user_input == "":
        # If the user pressed Enter, exit the loop using 'break'.
        break
    else:
        # If the user entered a number, convert it to an integer and add it to the 'sum'.
        sum += int(user_input)

# After the loop ends, thank the user for using the summing calculator and display the final sum.
print("Thank you for using summing calculator. The final sum was " + str(sum) + ".")
