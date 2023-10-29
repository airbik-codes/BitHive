'''
Name: Aakib Kibria Khan

Myseneca: akkhan9@myseneca.ca

Description: The code allows the user to input items, prices, and quantities for grocery shopping. 
It applies discounts to eligible items and generates a receipt with itemized details, 
including item names, quantities, prices, and total costs. 
It also calculates and displays the total cost of the purchases and the total discount applied.

'''
# Initializing the list of items that are eligible for promotional discounts.
discounted_items = ['candy', 'eggs', 'flour', 'hummus', 'ice cream', 'chicken soup', 'diapers']

# Initializing variables to store receipt and total_discount.
receipt = []              # Create an empty list to store item details for the receipt.
total_discount = 0        # Initialize a variable to store the total discount.

# Function to calculate the discount based on the number of items purchased.
def calculate_discount(quantity, price):
    discount = 0            # Initialize a discount variable.
    for i in range(quantity - 1):
        discount += price * 0.05  # Calculate a 5% discount for each item (up to a maximum of 20%).
        if discount >= price * 0.20:
            break         # If the discount exceeds or equals 20%, stop calculating.
    return discount

# Main program
print("Shopping Calculator")  # Display a title for the program.
while True:                  # Start an infinite loop to input items.
    user_input = input("Please enter an item of food, or press Enter to exit: ")
    
    if user_input == "":
        break             # If the user presses Enter, exit the loop.
    elif user_input.isalpha():
        item_name = user_input  # If the input is alphabetic, assume it's the item name.
    else:
        print("Please enter a valid name of a food item.")  # Display an error message.
    
    while True:              # Start a loop for entering the price, ensuring it's valid.
        price_input = input(f"Item is: {item_name}. Please enter the price for this item: ")
    
        if price_input.replace(".", "", 1).isdigit():
            item_price = float(price_input)  # If the input is a valid number, store it as the item price.
            break
        else:
            print("Error: Price must be a number. Example: 1, or 1.99")  # Display an error message.
        
    while True:              # Start a loop for entering the quantity, ensuring it's valid.
        quantity_input = input(f"Item is: {item_name}. How many will you purchase: ")
        if quantity_input.startswith("-"):
            print("Error: Number of items must be a positive integer.")  # Display an error message for negative values.
        elif quantity_input.isdigit():
            item_quantity = int(quantity_input)  # If the input is a positive integer, store it as the item quantity.
            break
        else:
            print("Error: Number of items must be a positive integer.")  # Display an error message.
        
    if item_name in discounted_items:
        item_discount = calculate_discount(item_quantity, item_price)  # Calculate the discount for eligible items.
        total_discount += item_discount  # Add the discount to the total discount.
        item_price -= item_discount    # Deduct the discount from the item price.
    
    line_item = f"{item_name:<10} {item_quantity:2} x $ {item_price:.2f} = $ {item_quantity * item_price:.2f}"
    # Create a line item string for the receipt with proper formatting.
    receipt.append(line_item)  # Add the line item to the receipt list.
    
# Print the receipt
print("\nRECEIPT")  # Display a title for the receipt.
for i in range(len(receipt)):  # Iterate over each item in the receipt.
    item = receipt[i]          # Get the item from the receipt list.
    print(f"{i + 1}. {item}")  # Display the item number and details.

total_cost = 0                  # Initialize a variable to store the total cost.
for line in receipt:            # Iterate over each line item in the receipt.
    parts = line.split('=')     # Split the line item into parts using '=' as a delimiter.
    quantity = int(parts[0].split('x')[0])  # Extract the quantity from the line item.
    price = float(parts[1].strip())         # Extract the price from the line item.
    total_cost += quantity * price         # Calculate and accumulate the total cost.

print(f"Total:                    $ {total_cost:.2f}")  # Display the total cost.
print(f"You saved:                 $ {total_discount:.2f}")  # Display the total discount.





        