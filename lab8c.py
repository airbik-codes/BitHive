'''
Name: Aakib Kibria Khan
ID: 157802224
Email: akkhan9@myseneca.ca

'''
import os  # Import the os module

# Run the 'whoami' command to get the current username and store it in a variable
userN = os.popen('whoami')
user_name = userN.read()  # Read the data and store the current user

# Print a welcome message with the username
print("Welcome, " + user_name, end="")

# Run the 'ping' command to test the network connectivity
network_test = os.system('ping -n 4 8.8.8.8 >nul 2>nul')

# Check if the network test command runs successfully (returns 0) and print the output
if network_test == 0:
    print("The Internet is UP.")

# Print a string indicating the uptime
print("uptime is:")

# Run the 'systeminfo' command and store the output in a variable
system_info = os.system('systeminfo >nul 2>nul')

# Print the system info variable data
print(system_info)
