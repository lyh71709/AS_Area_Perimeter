# Component 2 - implementing triangles
# v2 - puts some required input fields in the function to shorten the main routine

import math


# string_checker function goes here
# Ensures that an input is within the possible results
def string_checker(choice, options, error):
    for var_list in options:

        # if the snack is in one of the lists, return the full list
        if choice in var_list:

            # Get full name of snack and put it in title case
            # so it looks nice when out putted
            chosen = choice.title()
            is_valid = "yes"
            break

        # if the chosen snack is not valid, set snack_ok to no
        else:
            is_valid = "no"

    # If snack is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        print(error + "\n")
        return "invalid choice"

# triangle function goes here
# Figures out what the question gives and calculates the area and perimeter
def triangle():

    # Find what the user is looking for
    outcome = input("What do you want to find (Area or Perimeter)? ")
    outcome_check = string_checker(outcome, ["area", "perimeter"], "This must be either Area or Perimeter")
    print()

    # Find what the user is given
    info = input("What do you know about the triangle (bh or abc)? ")
    info_check = string_checker(info, ["bh", "abc"], "Please say either 'bh' for base and height or abc for side lengths")

    # Loop when error occurs
    valid = False
    while not valid:

        # If base and height is given
        if info_check == "Bh":
            # If the user is looking for perimeter
            if outcome_check == "perimeter":
                            print("I can't find the perimeter with only base and height because I don't have enough information")
                            return "Unable to calculate"
            # If the user is looking for area
            else:
                base = float(input("What is the base length? "))
                height = float(input("What is the height? "))
                
                area = 0.5 * base * height
                print("The area of your triangle is {}".format(area))
        # If triangle side lengths are given
        else:
            a = float(input("What is the length of a? "))
            b = float(input("What is the length of b? "))
            c = float(input("What is the length of c? "))
            # If user wants the area
            if outcome == "area":
                s = (a + b + c) / 2
                area = math.sqrt(s * (s-a) * (s-b) * (s-c))
                print("The area of your triangle is {}".format(area))
            # If the user is looking for perimeter
            else:
                perimeter = a + b + c
                print("The area of your triangle is {}".format(perimeter))
        # return this until I put in a lsit for history
        return("triangle", a, b, c, )


# Main Routine
# Possible Shapes
shape_types = ["square", "rectangle", "parallelogram", "triangle", "circle", "trapezium"]

# Find the shape
what_shape = input("What shape do you want? ").lower()
check_shape = string_checker(what_shape, shape_types, "Please enter a real shape")

# Triangle Scenario
if check_shape == "Triangle":
    result = triangle()
