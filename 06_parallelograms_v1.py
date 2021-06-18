# Component 6 - implement parallelogram function

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
            chosen = var_list.title()
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
        info = input("What do you want to find out [Area(a)] or [Perimeter(p)] or [Both(b)]? ").lower()
        info_check = string_checker(info, ["a", "p", "b"], "Please say either 'a' for area or 'p' for perimeter")
        if info_check == "invalid choice":
            continue
        
        # Get base
        base = number_checker("What is the base? ", "Please enter a number above 0", float)

        # ------------- Calculations -------------
        # Only area scenario
        if info_check == "A":
            # Find only height and area
            height = number_checker("What is the height? ", "Please enter a number above 0", float)
            area = base * height
            print("The area of your parallelogram is {:.2f}".format(area))
        # Only perimeter scenario
        elif info_check == "P":
            # Find only side and perimeter
            side = number_checker("What is the side length? ", "Please enter a number above 0", float)
            perimeter = 2 * (side + base)
            print("The perimeter of your parallelogram is {:.2f}".format(perimeter))
        # Both cases
        else:
            # Find height and side as well as area and perimeter
            height = number_checker("What is the height? ", "Please enter a number above 0", float)
            side = number_checker("What is the side length? ", "Please enter a number above 0", float)
            area = base * height
            perimeter = 2 * (side + base)
            print("The area of your parallelogram is {:.2f}".format(area))
            print("The perimeter of your parallelogram is {:.2f}".format(perimeter))
        print()

        # return this until I put in a list for history
        return ""

# Main Routine

what_shape = "parallelogram"

for item in range(0,3):
    if what_shape == "parallelogram":
        result = parallelogram()
