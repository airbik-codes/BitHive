'''
Name: Aakib Kibria Khan
ID:157802224
Email: akkhan9@myseneca.ca
'''

from lab7b import print_meal_plan


template = {'breakfast': None, 'lunch': None, 'dinner': None}
days = []
if __name__=='__main__':
    while True:
        add_day = input("Would you like to add a day? (y/n): ")
        if add_day.lower() == 'n':
            break

        new_day = template.copy()
        for meal in new_day:
            new_day[meal] = input(f"Please enter what you would like to eat for {meal}: ")

        days.append(new_day)

    num_of_days = len(days)

    if num_of_days == 0:
        print("You haven't added any days.")
    else:
        day_num = int(input(f"Please enter a day number for the menu you would like to print (1-{num_of_days}): "))
        if 1 <= day_num <= num_of_days:
            print_meal_plan(days[day_num - 1])
        else:
            print("Error: Day number is out of range.")