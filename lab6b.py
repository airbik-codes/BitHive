'''''''''
Name: Aakib Kibria Khan
ID:157802224
Email: akkhan9@myseneca.ca

'''''''''

# Import the sys module to access command-line arguments.
import sys

# Check if there are command-line arguments (sys.argv) provided.
if len(sys.argv) > 1:
    # If there are command-line arguments, open the file specified as the first argument ('sys.argv[1]') in read ('r') mode.
    file = open(sys.argv[1], 'r')
else:
    # If there are no command-line arguments, open a file named 'readme.txt' in read ('r') mode.
    file = open('readme.txt', 'r')

# Read all the lines from the file and store them as a list of strings in the 'data' variable.
data = file.readlines()

# Close the file to free up system resources.
file.close  # This line is missing '()' to actually call the 'close' method. It should be 'file.close()'.

# Reverse the order of lines in the 'data' list.
data.reverse()

# Iterate over each line (string) in the 'data' list.
for i in data:
    # Print each line (with leading and trailing whitespaces removed) to the console.
    print(i.strip())


