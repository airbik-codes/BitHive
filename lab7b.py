'''
Name: Aakib Kibria Khan
ID:157802224
EmaiL: akkhan9@myseneca.ca

'''

# Create a dictionary representing a meal plan with keys like 'breakfast', 'lunch', 'dinner', and 'snack'.
meal_plan = {'breakfast': 'soup', 'lunch': 'tofu', 'dinner': 'pizza', 'snack': 'cookies'}

# Define a function named 'print_meal_plan' that takes a dictionary ('meal_dict') as a parameter and prints a formatted meal plan.
def print_meal_plan(meal_dict):
    # Set the width of the output to 50 characters.
    width = 50
    
    # Create a title string for the meal plan with centered text within the specified width.
    meal_str = f"{'MENU FOR TODAY' : ^{width}}\n"
    
    # Add a line of equal signs as a separator.
    meal_str += f"=" * width + "\n"
    
    # Add lines for each meal category (breakfast, lunch, dinner) with corresponding food items.
    meal_str += f"{'Breakfast':<{width//2}}{meal_dict['breakfast']:>{width//2}}\n"
    meal_str += f"{'Lunch':<{width//2}}{meal_dict['lunch']:>{(width//2)}}\n"
    meal_str += f"{'Dinner':<{width//2}}{meal_dict['dinner']:>{(width//2)}}\n"

    # Print the generated meal plan.
    print(meal_str)


# print_meal_plan(meal_plan)
