# Component 3 - implementing triangles
# v2 - puts some required input fields in the function to shorten the main routine and implement the number checker in.
# v3 - change up some wording to make the program more usable
# v4 - doesn't ask for area or perimeter and just prints both

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

# triangle function goes here
# Figures out what the question gives and calculates the area and perimeter
def triangle():

    valid = False
    while not valid:

        # Find what the user is given
        info = input("What do you know about the triangle [Base and height(bh)] or [the side lengths(abc)]? ").lower()
        info_check = string_checker(info, ["bh", "abc"], "Please say either 'bh' for base and height or 'abc' for side lengths")
        if info_check == "invalid choice":
            continue

        # ------------- Calculations -------------
        # If base and height is given
        if info_check == "Bh":

            base = number_checker("What is the base? ", "Please enter a number bigger than 0", float)
            height = number_checker("What is the height? ", "Please enter a number bigger than 0", float)
                
            area = 0.5 * base * height

            print("The area of your triangle is {:.2f}".format(area))
            print("I can't find the perimeter with only base and height")

        # If triangle side lengths are given
        else:
            a = number_checker("What is the length of a? ", "Please enter a number bigger than 0", float)
            b = number_checker("What is the length of b? ", "Please enter a number bigger than 0", float)
            c = number_checker("What is the length of c? ", "Please enter a number bigger than 0", float)

            # Do Heron's Law and the sum of all the side lengths for perimeter
            s = (a + b + c) / 2
            perimeter = a + b + c
            area = math.sqrt(s * (s-a) * (s-b) * (s-c))

            print("The area of your triangle is {:.2f}".format(area))
            print("The perimeter of your triangle is {:.2f}".format(perimeter))

    # return this until I put in a list for history
    return ""


# Main Routine
# Set the shape as triangle to make testing easier seeing as how this is the triangle component
what_shape = "Triangle"

# Loop for testing purposes
for item in range(0,4):
    # Triangle Scenario
    if what_shape == "Triangle":
        result = triangle()
    print()
