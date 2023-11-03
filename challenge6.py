'''
Name:Aakib Kibria Khan
ID: 157802224
Email: akkhan9@myseneca.ca

'''

# Import the sys module to access command-line arguments.
import sys

# Check if there is at least one command-line argument provided.
if len(sys.argv) < 2:
    # If not enough arguments are provided, print a usage message.
    print('Usage: challenge6.py target')
else:
    try:
        # Attempt to open the file specified as the first argument ('sys.argv[1]') in read ('r') mode.
        file = open(sys.argv[1], 'r')
    except FileNotFoundError:
        # If the file is not found, print an error message.
        print(f'ERROR: {sys.argv[1]} not found')
    
    # Read all the lines from the file and store them as a list of strings in the 'data' variable.

    data = file.readlines()

    # Iterate over each line (string) in the 'data' list.
    for i in data:
        # Convert the line to lowercase and then create a list of its characters.
        arr = list(i.lower())
        # Initialize the 'largest' variable with 'a'.
        largest = 'a'

        # Iterate over the characters in the 'arr' list.
        for j in range(len(arr)):
            # Compare the current character with the current largest character ('largest').
            if arr[j] > largest:
                # Update 'largest' if the current character is larger.
                largest = arr[j]

        # Print the largest character found in the current line.
        print(largest)
