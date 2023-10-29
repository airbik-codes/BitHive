
'''
Name: Aakib Kibria Khan
Student_ID: 157802224
'''

# Import the math module to use pi
import math

# Define a function to calculate the area of a circle based on its radius
def circle_area(radius):
    area = math.pi * (radius ** 2)  # Calculate the area using the formula for a circle
    return area

# Main program
if __name__ == "__main__":
    print("Circle Area Calculator")
    
    # Continuous loop until the user decides to exit
    while True:
        user_input = input("Enter a radius between 0 and 1999. Press Enter to exit: ")
        
        # Check if the user pressed Enter to exit
        if user_input == "":
            break
        
        # Check if the user input is a numeric value
        if user_input.isnumeric():
            # Convert the user input to an integer
            radius = int(user_input)
            
            # Check if the entered radius is within the specified range
            if 0 <= radius <= 1999:
                # Calculate the area using the circle_area function and print the result
                area = circle_area(radius)
                print(f"Radius: {radius}. Area: {area}.")
            else:
                print(f"Error: {user_input} is out of range.")
        else:
            print(f"Error: {user_input} is not a number.")
print("Exiting...")


