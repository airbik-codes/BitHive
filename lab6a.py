'''
Name: Aakib Kibria Khan
Student_ID: 157802224
Email: akkhan9@myseneca.ca

'''

# Create a list called 'data_to_write' with four string elements.
data_to_write = ['First Line!', 'Second Line!!', 'Third Line!!!', '...and so on!']

# Open a file named 'testing.txt' in write ('w') mode. 
file = open('testing.txt', 'w')

# Iterate over each element (line) in the 'data_to_write' list.
for i in data_to_write:
    # Write the current element (line) followed by a newline character ('\n') to the 'testing.txt' file.
    file.write(i + '\n')

# Close the 'testing.txt' file to ensure changes are saved.
file.close()
