'''
Name: Aakib Kibria Khan
ID: 157802224
Email: akkhan9@myseneca.ca

'''

# Create a dictionary representing student information with keys like 'first_name', 'last_name', 'addr1', 'city', 'prov', and 'pcode'.
student1 = {'first_name': 'eric', 'last_name':'smith', 'addr1': '217 Au Large Blvd', 'city': 'Toronto', 'prov': 'Ontario', 'pcode': 'M4A 1P3'}

# Define a function named 'shipping_label' that takes a dictionary ('a_lst') as a parameter and generates a formatted string.
def shipping_label(a_lst):
    "takes a list, generates a string"
    # Build the first line of the address string by capitalizing the first and last name from the dictionary.
    a_str = f"{a_lst['first_name'].capitalize()} {a_lst['last_name'].capitalize()}\n"
    
    # Add the second line of the address string with the address line 1 from the dictionary.
    a_str += f"{a_lst['addr1']}\n"
    
    # Add the third line of the address string with the city and province from the dictionary.
    a_str += f"{a_lst['city']}, {a_lst['prov']}\n"
    
    # Add the fourth line of the address string with the postal code from the dictionary.
    a_str += f"{a_lst['pcode']}"
    
    # Return the generated address string.
    return a_str

# Uncomment the next lines if this script is meant to be executed independently.
# if __name__ =='__main__':
# Call the 'shipping_label' function with the 'student1' dictionary and store the result in the 'label' variable.
label = shipping_label(student1)

# Print the generated address label.
print(label)
