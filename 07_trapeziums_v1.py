# Component 6 - implement trapezium function
# v2 - The previous component was just a basic three if conditions and then ask accordingly
#      But I prefer this method because personally even though it might basically be the same length it is more clean and neat.

import math

# number checker function goes here
# Checks that it is not 0 and is a number
def number_checker(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))
        
            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# string_checker function goes here
# Ensures that an input is within the possible results
def string_checker(choice, options, error):
    for var_list in options:

        # Blank case
        if choice == "":
            is_valid = "no"
            break 
        # if the shape is in one of the lists, return the full list
        elif choice in var_list:

            # Get full name of shape and put it in title case
            # so it looks nice when out putted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen shape is not valid
        else:
            is_valid = "no"

    # If shape is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        print(error)
        return "invalid choice"

# trapezium function goes here
# Find the base, height and side length then calculate area and perimeter
def trapezium():
    valid = False
    while not valid:

        # Find what the user is looking for
        info = input("What do you want to find out [Area(a)] or [Perimeter(p)] or [Both(ap)]? ").lower()
        info_check = string_checker(info, [["a "], [" p"], ["ap"]], "Please say either 'a' for area or 'p' for perimeter")
        print(info_check)
        if info_check == "invalid choice":
            continue
        
        # base is needed in all cases so it is outside the if statement
        base_a = number_checker("What is the first base? ", "Please enter a number above 0", float)
        base_b = number_checker("What is the second base? ", "Please enter a number above 0", float)
        # Check if user wants area
        if info_check[1] == "p" or info_check[1] == "P":
            side_c = number_checker("What is the first side length? ", "Please enter a number above 0", float)
            side_d = number_checker("What is the second side length? ", "Please enter a number above 0", float)
            # Check if user wants perimeter as well
            if info_check[0] == "A":
                height = number_checker("What is the height? ", "Please enter a number above 0", float)
            # If only area
            else:
                height = 0
        # Perimeter scenario
        else:
            height = number_checker("What is the height? ", "Please enter a number above 0", float)
            side_c = 0
            side_d = 0
        
        # ------------- Calculations -------------
        area = ((base_a + base_b)/2) * height
        perimeter = base_a + base_b + side_c + side_d

        # Area
        if height != 0:
            print("The area of your trapezium is {:.2f}".format(area))
            # Perimeter as well
            if side_c != 0:
                print("The perimeter of your trapezium is {:.2f}".format(perimeter))
        # Perimeter only
        else:
            print("The perimeter of your trapezium is {:.2f}".format(perimeter))
        print()
        # return this until I put in a list for history
        return ""

# Main Routine

what_shape = "trapezium"

# Loop for testing purposes
for item in range(0,3):
    if what_shape == "trapezium":
        result = trapezium()
        