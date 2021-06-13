# Component 4 - implement rectangle function

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

# rectangle function goes here
# Find the base and height then calculate area and perimeter
def rectangle():
    valid = False
    while not valid:
        
        base = number_checker("What is the base? ", "Please enter a number above 0", float)
        height = number_checker("What is the height? ", "Please enter a number above 0", float)

        area = base * height
        perimeter = (2 * base) + (2 * height)

        if base == height:
            squ_or_rec = "square"
        else:
            squ_or_rec = "rectangle"

        print("The area of your {} is {:.2f}".format(squ_or_rec, area))
        print("The perimeter of your {} is {:.2f}".format(squ_or_rec, perimeter))

# Main Routine

what_shape = "Rectangle"

# loop for testing purposes
for item in range(0,1):
    if what_shape == "Rectangle":
        result = rectangle()
        print()