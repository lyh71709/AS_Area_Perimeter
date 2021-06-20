# Component 6 - implement parallelogram function
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

# parallelogram function goes here
# Find the base, height and side length then calculate area and perimeter
def parallelogram():
    valid = False
    while not valid:

        # Find what the user is looking for
        info = input("What do you want to find out [Area(a)] or [Perimeter(p)] or [Both(ap)]? ").lower()
        info_check = string_checker(info, [["a "], [" p"], ["ap"]], "Please say either 'a' for area or 'p' for perimeter")
        if info_check == "invalid choice":
            continue
        
        # base is needed in all cases so it is outside the if statement
        base = number_checker("What is the base? ", "Please enter a number above 0", float)
        # Check if user wants area
        if info_check[0] == "A":
            height = number_checker("What is the height? ", "Please enter a number above 0", float)
            # Check if user wants perimeter as well
            if info_check[1] == "p":
                side = number_checker("What is the side length? ", "Please enter a number above 0", float)
            # If only area
            else:
                side = 0
        # Perimeter scenario
        else:
            side = number_checker("What is the side length? ", "Please enter a number above 0", float)
            height = 0
        
        # ------------- Calculations -------------
        area = base * height
        perimeter = 2 * (side + base)

        # Area
        if height != 0:
            print("The area of your parallelogram is {:.2f}".format(area))
            # Perimeter as well
            if side != 0:
                print("The perimeter of your parallelogram is {:.2f}".format(perimeter))
        # Perimeter only
        else:
            print("The perimeter of your parallelogram is {:.2f}".format(perimeter))
        print()
        # return this until I put in a list for history
        return ""

# Main Routine

what_shape = "parallelogram"

# Loop for testing purposes
for item in range(0,3):
    if what_shape == "parallelogram":
        result = parallelogram()
