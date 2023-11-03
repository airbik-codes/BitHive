'''
Name: Aakib Kibria Khan
ID: 157802224
Email: akkhan9@myseneca.ca

'''

# Import the sys module to access command-line arguments.
import sys

# Check if there are at least 3 command-line arguments provided.
if len(sys.argv) < 3:
    # If not enough arguments are provided, print a usage message.
    print(f'Usage: {sys.argv[0]} keyword filename')
else:
    try:
        # Attempt to open the file specified as the second argument ('sys.argv[2]') in read ('r') mode.
        file = open(sys.argv[2], 'r')
    except FileNotFoundError:
        # If the file is not found, print an error message and exit the program with a non-zero status code.
        print(f'ERROR: {sys.argv[2]} not found.')
        sys.exit(1)

    # Read all the lines from the file and store them as a list of strings in the 'data' variable.
    data = file.readlines()
    # Initialize a count variable to keep track of the line number.
    count = 1

    # Iterate over each line (string) in the 'data' list.
    for i in data:
        # Check if the keyword specified as the first argument ('sys.argv[1]') is in the current line.
        if sys.argv[1] in i:
            # If the keyword is found in the line, print the line number and the line (with leading and trailing whitespaces removed).
            print(f'{count}: {i.strip()}')
        # Increment the count variable for the next line.
        count += 1
