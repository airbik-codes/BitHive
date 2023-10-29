'''
Name: Aakib Kibria Khan
Student_ID: 157802224
'''
import random

def rtrn_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (int): The length of the rectangle.
        width (int): The width of the rectangle.

    Returns:
        int: The area of the rectangle.
    """
    return length * width

rect = rtrn_area(5, 3)

def print_all_caps(name, age):
    """
    Print a person's name in all capital letters and their age.

    Args:
        name (str): The name of the person.
        age (int): The age of the person.
    """
    cap_name = name.upper()
    print("This person's name is " + cap_name + " and THEY ARE " + str(age) + " YEARS OLD!!!")

print_all_caps('eric', 41)
print_all_caps('melissa', 40)

def get_rando():
    """
    Generate a random integer between 1 and 100.

    Returns:
        int: A random integer between 1 and 100.
    """
    return random.randint(1, 101)

lucky_num = get_rando()

def is_odd(num):
    """
    Check if a number is odd.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    """
    if num % 2 == 1:
        return True
    else:
        return False

print(is_odd(13))
print(is_odd(get_rando()))
