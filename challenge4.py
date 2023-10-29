'''
Name: Aakib Kibria Khan
Student_ID: 157802224
'''
# Define a function to calculate the slope between two points.
def rtrn_slope(x1, x2, y1, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope

# Main program execution starts here.
if __name__ == "__main__":
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

    # Loop to input and process point coordinates.
    while True:
        user_input = input("Enter the starting X value or press Enter to quit: ")
        if user_input == "":
            break
        if user_input.isnumeric():
            if 0 <= int(user_input) <= 10:
                x1 = int(user_input)
            else:
                print(f"Error: {user_input} is out of range.")
        else:
            print(f"Error: {user_input} is not a number.")

        user_input = input("Enter the next Y value or press Enter to quit: ")
        if user_input == "":
            break
        if user_input.isnumeric():
            if 0 <= int(user_input) <= 10:
                y1 = int(user_input)
            else:
                print(f"Error: {user_input} is out of range.")
        else:
            print(f"Error: {user_input} is not a number.")

        user_input = input("Enter the new X value or press Enter to quit: ")
        if user_input == "":
            break
        if user_input.isnumeric():
            if 0 <= int(user_input) <= 10:
                x2 = int(user_input)
            else:
                print(f"Error: {user_input} is out of range.")
        else:
            print(f"Error: {user_input} is not a number.")

        user_input = input("Enter the new Y value or press Enter to quit: ")
        if user_input == "":
            break
        if user_input.isnumeric():
            if 0 <= int(user_input) <= 10:
                y2 = int(user_input)
            else:
                print(f"Error: {user_input} is out of range.")
        else:
            print(f"Error: {user_input} is not a number.")
        
        # Calculate and display the slope between the two points.
        final_slope = rtrn_slope(x1, x2, y1, y2)
        print(f"Slope is: {final_slope}")

    # Program exits when the user decides to quit.
    print("Exiting...")










