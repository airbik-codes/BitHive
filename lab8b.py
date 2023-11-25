'''
Name: Aakib Kibria Khan
ID: 157802224
Email: akkhan9@myseneca.ca

'''
import sys
import re

def find_phone_numbers(filename):
    # Open the specified file in read mode
    with open(filename, 'r') as file:
        # Read the content of the file
        text = file.read()

        # Define the regular expression pattern for matching phone numbers
        phone_pattern = r'\d{3}-\d{3}-\d{4}'
        
        # Use the findall() method to find all phone numbers in the text
        phone_numbers = re.findall(phone_pattern, text)
    
    # Return the list of phone numbers
    return phone_numbers
    
# Check if the correct number of command line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python lab8b.py <filename>")
    sys.exit(1)

# Get the filename from the command line argument
filename = sys.argv[1]

# Call the find_phone_numbers function to extract phone numbers from the file
phone_numbers = find_phone_numbers(filename)

# Print the number of phone numbers found
print(f"Number of phone numbers found: {len(phone_numbers)}")

# Ask the user if they want to see the results
user_input = input("Do you want to see the results? (y/n): ")

# Check user input and print phone numbers accordingly
if user_input.lower() in ('y', 'yes', ''):
    for number in phone_numbers:
        print(number)
elif user_input.lower() in ('n', 'no'):
    print("Program terminated.")
else:
    print("Invalid input. Program terminated.")
