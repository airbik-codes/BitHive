'''
Name: Aakib Kibria Khan
ID:157802224
Email: akkhan9@myseneca.ca

'''

# Import the 'csv' module for reading and writing CSV files and the 'sys' module for interacting with the Python interpreter.
import csv
import sys

# Define a function 'read_csv' that takes a filename as input and returns a list of dictionaries read from the CSV file.
def read_csv(filename):
    '''Input file name and return a list'''
    list_of_dicts = []
    # Open the CSV file in read mode.
    f = open(filename, 'r')
    # Create a CSV reader object to read the file as a dictionary.
    reader = csv.DictReader(f)
    # Iterate over each row in the CSV file and append it as a dictionary to the list.
    for row in reader:
        list_of_dicts.append(row)
    # Close the file.
    f.close()
    # Return the list of dictionaries.
    return list_of_dicts

# Define a function 'write_csv' that takes a filename and data (list of dictionaries) as input and writes the data to a CSV file.
def write_csv(filename, data):
    # Open the CSV file in write mode with newline='' to handle newline characters properly.
    f = open(filename, 'w', newline='')
    # Create a CSV writer object.
    writer = csv.writer(f)
    
    # Check if there is data to write.
    if data:
        # Write the header row using the keys from the first dictionary in the data list.
        writer.writerow(data[0].keys())
        # Write each row of values from the dictionaries in the data list.
        for row in data:
            writer.writerow(row.values())
    
    # Close the file.
    f.close()

# Define a function 'substitute_data' that takes a list of dictionaries ('data') and substitutes specific values.
def substitute_data(data):
    for row in data:
        # Check and substitute specific values in each dictionary.
        if row.get('First Name') == 'Christopher':
            row['First Name'] = 'Chris'
        if row.get('Last Name') == 'Patal':
            row['Last Name'] = 'Patel'
        if row.get('Last Name') == 'Smith':
            row['Last Name'] = 'Nichols'
        if row.get('Address') == '81 Vanier':
            row['Address'] = '72 Princeton'
        if row.get('Last Name') == 'Geary':
            row['Address'] = '455 Bloor'
        if row.get('City') == 'North York':
            row['City'] = 'Toronto'
        if row.get('Country') == 'Canada':
            row['Country'] = 'CA'

# Check if the script is being executed as the main program.
if __name__ == '__main__':
    # Check if the correct number of command-line arguments is provided.
    if len(sys.argv) != 2:
        print("Usage: python lab7d.py <filename>")
        sys.exit(1)

    # Get the filename from the command-line arguments.
    filename = sys.argv[1]
    
    # Call the 'read_csv' function to read data from the CSV file.
    data = read_csv(filename)
    
    # Call the 'substitute_data' function to substitute specific values in the data.
    substitute_data(data)
    
    # Call the 'write_csv' function to write the modified data back to the CSV file.
    write_csv(filename, data)
