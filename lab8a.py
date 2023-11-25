'''
Name: Aakib Kibria Khan
ID:157802224
Email: akkhan9@myseneca.ca

'''

import re

# Define a regular expression pattern for matching phone numbers in the format "###-###-####"
tel_num = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Use the findall() method to find all occurrences of the pattern in the given text
mo = tel_num.findall("My telephone number is 555-877-5678. Or you can reach me on my cell: 555-212-0771. Call me!")

# Iterate through the matches found and print each phone number
for match in mo:
    print("Found phone number: " + match)
