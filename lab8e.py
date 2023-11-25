'''
Name: Aakib Kibria Khan
ID: 157802224
Email: akkhan9@myseneca.ca
'''
import os
import sys
import shutil

def create_backup(directory):
    try:
        # Get the absolute path of the user-defined directory
        user_directory = os.path.abspath(directory)

        # Create the 'backups' directory if it doesn't exist
        backup_directory = os.path.join(user_directory, 'backups')
        if not os.path.exists(backup_directory):
            os.makedirs(backup_directory)

        # Walk through the user-defined directory and its subdirectories
        for root, dirs, files in os.walk(user_directory):
            for file in files:
                # Check if the file is a Python script (ends with '.py')
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    # Copy the Python script to the 'backups' directory
                    shutil.copy(file_path, backup_directory)

        print("Backup completed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python lab8e.py <directory>")
        sys.exit(1)

    # Get the directory from the command line argument
    directory = sys.argv[1]

    # Check if the specified directory is a valid directory
    if not os.path.isdir(directory):
        print("Error: Not a valid directory.")
        sys.exit(1)

    # Call the create_backup function with the specified directory
    create_backup(directory)

if __name__ == "__main__":
    # Execute the main function when the script is run
    main()
