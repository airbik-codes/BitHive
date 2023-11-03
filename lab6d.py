'''
Name:Aakib Kibria Khan
ID:157802224
Email: akkhan9@myseneca.ca

'''

# Import the sys module to access command-line arguments.
import sys

# Check if there is at least one command-line argument provided.
if len(sys.argv) < 2:
    # If not enough arguments are provided, print a usage message.
    print("Usage: lab6d.py target")
else:
    try:
        # Attempt to open the file specified as the first argument ('sys.argv[1]') in read ('r') mode.
        file = open(sys.argv[1], 'r')
    except:
        # If an error occurs while trying to open the file, print an error message and exit the program with a non-zero status code.
        print(f'ERROR: {sys.argv[1]} not found')
        sys.exit(1)

    # Read all the lines from the file and store them as a list of strings in the 'data' variable.
    data = file.readlines()
    # Close the file to free up system resources.
    file.close()

    # Reopen the same file in write ('w') mode to overwrite its contents.
    file = open(sys.argv[1], 'w')
    
    # Iterate over each line (string) in the 'data' list.
    for i in data:
        sum = 0.0
        # Split the current line into a list of values using space (' ') as the separator.
        line = i.split(' ')
        line_rm = []
        
        # Iterate over each value in the 'line' list.
        for j in line:
            try:
                # Try to convert the value to a float and add it to the 'sum'.
                sum = sum + float(j)
            except:
                # If conversion to float fails, it means the value is not a number, so add it to the 'line_rm' list with a space.
                line_rm.append(j + ' ')
        
        # Remove the trailing space from the last value in the 'line_rm' list.
        line_rm[len(line_rm) - 1] = line_rm[len(line_rm) - 1].strip()
        
        # Write the cleaned line (with non-numeric values and extra spaces removed) to the file.
        for j in line_rm:
            file.write(j)
        
        # Add a newline character to separate lines.
        file.write('\n')
        
        # Print the sum of numeric values in the current line.
        print(sum)
