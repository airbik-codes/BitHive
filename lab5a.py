'''
Name:Aakib Kibria Khan
ID:157802224
email:akkhan9@myseneca.ca


'''



def my_sum(user_numbers):
    # Initialize a variable 'sum' to store the sum of user_numbers
    sum = 0

    # Iterate through each number in user_numbers
    for number in user_numbers:
        # Add the current number to the 'sum' variable
        sum = sum + number

    # Return the final sum
    return sum

if __name__ == "__main__":
    user_numbers = []  # Initialize an empty list to store user input
    print("SUMMING CALCULATOR")

    while True:
        # Get user input (a number) or an empty string to exit
        user_input = input("Enter a number to add to your sum. Pressing Enter will exit. ")
        
        if user_input == "":
            break  # Exit the loop if the user presses Enter without entering a number
        else:
            # Convert the user input to an integer and append it to the user_numbers list
            user_numbers.append(int(user_input))
            
            # Calculate the sum of user_numbers using the my_sum function
            num_sum = my_sum(user_numbers)
            
            # Get the length (count) of user_numbers
            num_length = len(user_numbers)
            
            # Calculate the average by dividing the sum by the count
            average = num_sum / num_length
            
            # Print the sum, count, and average
            print(f"Total sum is: {num_sum}. Total count is: {num_length}. Average for this list is: {average}. ")
    
    # Print a thank-you message when the user exits the loop
    print("Thank you for using average calculator.")




  