'''
Name: Aakib Kibria Khan
ID: 157802224
Email: akkhan9@myseneca.ca

'''
import os  # Import the os module

# Specify the course directory as a relative path
course_dir = '..'

# Print the absolute path of the course directory
print('Your current directory is: ' + os.path.abspath(course_dir))

# Walk through the directory and print the path of each file
for root, directories, filenames in os.walk(course_dir):
    for file in filenames:
        print(os.path.join(root, file))
