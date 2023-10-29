'''
Name:Aakib Kibria Khan
ID:157802224
email:akkhan9@myseneca.ca


'''


import sys

# Check if there are at least two command-line arguments (script name + at least one number)
if len(sys.argv) < 2:
    print("Usage: Enter one or more command line arguments.")
    sys.exit(1)

# Initialize variables to store the sum and count of valid numbers
total = 0
count = 0

# Initialize a list to store found numbers for later display
found_numbers = []

# Loop through command-line arguments starting from the second element (skipping the script name)
for arg in sys.argv[1:]:
    if arg.isdigit():  # Check if the argument is a non-negative integer
        number = int(arg)
        total += number
        count += 1
        found_numbers.append(number)
    else:
        # Handle non-numeric arguments
        print(f"Error: {arg} is not a number.")

# Check if no valid numbers were provided
if count == 0:
    print("No valid numbers provided.")
    sys.exit(1)

# Calculate the average of valid numbers
average = total / count

# Print found numbers and average
print("Number found:", ", ".join(map(str, found_numbers)))
print(f"Average for {count} numbers: {average:.1f}")

import sys

# Check if there are at least two command-line arguments (script name + at least one number)
if len(sys.argv) < 2:
    print("Usage: Enter one or more numbers separated by commas.")
    sys.exit(1)

# Initialize variables to store the sum and count of valid numbers
total = 0
count = 0

# Initialize a list to store found numbers for later display
found_numbers = []

# Split the input string by commas and iterate through the resulting values
for arg in ','.join(sys.argv[1:]).split(','):
    if arg.isdigit():  # Check if the argument is a non-negative integer
        number = int(arg)
        total += number
        count += 1
        found_numbers.append(number)
    else:
        # Handle non-numeric arguments
        print(f"Error: {arg} is not a valid number.")

# Check if no valid numbers were provided
if count == 0:
    print("No valid numbers provided.")
    sys.exit(1)

# Calculate the average of valid numbers
average = total / count

# Print found numbers and average
print("Number found:", ", ".join(map(str, found_numbers)))
print(f"Average for {count} numbers: {average:.15f}")  # Increased precision for average





