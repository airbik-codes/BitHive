'''
Name: Aakib Kibria Khan
ID: 157802224
Email: akkhan9@myseneca.ca

'''

import csv
import sys

def read_csv(filename):
    '''Input file name and return a list'''
    list_of_dicts = []
    f = open(filename, 'r')
    reader = csv.DictReader(f)
    for row in reader:
        list_of_dicts.append(row)
    f.close()
    return list_of_dicts

def write_csv(filename, data):
    f = open(filename, 'w', newline='')
    writer = csv.writer(f)
    
    if data:
        writer.writerow(data[0].keys())
        for row in data:
            writer.writerow(row.values())
    
    f.close()

def substitute_data(data):
    for row in data:
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

# New function to print the modified table with keys for column titles.
def print_modified_table(data):
    if not data:
        print("No data to display.")
        return
    
    # Get the keys (column titles) from the first dictionary in the data list.
    keys = data[0].keys()

    # Print the column titles with proper formatting.
    print("|".join(f"{key:<12}" for key in keys))
    print("-" * (13 * len(keys) - 1))  # Separator line

    # Print each row of values with proper formatting.
    for row in data:
        print("|".join(f"{value:<12}" for value in row.values()))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python lab7d.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    data = read_csv(filename)
    substitute_data(data)
    write_csv(filename, data)

    # Call the new function to print the modified table.
    print_modified_table(data)
