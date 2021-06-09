# Component 2 - implementing triangles

import math

# string_checker function goes here
# Ensures that an input is within the possible results
def string_checker(choice, options, error):
    for var_list in options:

        # if the shape is in one of the lists, return the full list
        if choice in var_list:

            # Get full name of shape and put it in title case
            # so it looks nice when out putted
            chosen = choice.title()
            is_valid = "yes"
            break

        # if the chosen shape is not valid
        else:
            is_valid = "no"

    # If shape is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        print(error + "\n")
        return "invalid choice"

# triangle function goes here
# Figures out what the question gives and calculates the area and perimeter
def triangle(info_type, result):
    
    # Loop
    valid = False
    while not valid:

        # When base and height is given
        if info_type == "Bh":

            # When user wants the perimeter can't calculate
            if result == "perimeter":
                            print("I can't find the perimeter with only base and height because I don't have enough information")
                            return "Unable to calculate"
            # When user wants the area
            else:
                base = float(input("What is the base length? "))
                height = float(input("What is the height? "))
                
                area = 0.5 * base * height
                print("The area of your triangle is {}".format(area))
                # return incase I need to use it in a list later on
                return("triangle", base, height, area)

        # When triangle sides are given
        else:
            a = float(input("What is the length of a? "))
            b = float(input("What is the length of b? "))
            c = float(input("What is the length of c? "))

            # When user wants area
            if result == "area":
                # Use Heron's law
                s = (a + b + c) / 2
                area = math.sqrt(s * (s-a) * (s-b) * (s-c))
                print("The area of your triangle is {}".format(area))
                # return incase I need to use it in a list later on
                return("triangle", a, b, c, area)
            # When user want perimeter
            else:
                perimeter = a + b + c
                print("The area of your triangle is {}".format(perimeter))
                # return incase I need to use it in a list later on
                return("triangle", a, b, c, perimeter)


# Main Routine

# Set up shape types
shape_types = ["square", "rectangle", "parallelogram", "triangle", "circle", "trapezium"]

# Get the shape type
what_shape = input("What shape do you want? ").lower()
check_shape = string_checker(what_shape, shape_types, "Please enter a real shape")

# Triangle scenario
if check_shape == "Triangle":

    # Find out what information the user wants
    triangle_outcome = input("What do you want to find (Area or Perimeter)? ")
    triangle_outcome_check = string_checker(triangle_outcome, ["area", "perimeter"], "This must be either Area or Perimeter")
    print()

    # Find out what the user knows
    triangle_info = input("What do you know about the triangle (bh or abc)? ")
    triangle_info_check = string_checker(triangle_info, ["bh", "abc"], "Please say either 'bh' for base and height or abc for side lengths")
    triangle_calc = triangle(triangle_info_check, triangle_outcome)
