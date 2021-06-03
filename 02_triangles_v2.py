# Component 2 - implementing triangles

import math

# Number checker function goes here
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
def triangle(info_type, result):

    valid = False
    while not valid:

        if info_type == "Bh":

            if result == "perimeter":
                            print("I can't find the perimeter with only base and height because I don't have enough information")
                            return "Unable to calculate"
            else:
                base = float(input("What is the base length? "))
                height = float(input("What is the height? "))
                
                area = 0.5 * base * height
                print("The area of your triangle is {}".format(area))
                return("triangle", base, height, area)

        else:
            a = float(input("What is the length of a? "))
            b = float(input("What is the length of b? "))
            c = float(input("What is the length of c? "))

            if result == "area":
                s = (a + b + c) / 2
                area = math.sqrt(s * (s-a) * (s-b) * (s-c))
                print("The area of your triangle is {}".format(area))
                return("triangle", a, b, c, area)
            else:
                perimeter = a + b + c
                print("The area of your triangle is {}".format(perimeter))
                return("triangle", a, b, c, perimeter)


# Main Routine
shape_types = ["square", "rectangle", "parallelogram", "triangle", "circle", "trapezium"]

what_shape = input("What shape do you want? ").lower()
check_shape = string_checker(what_shape, shape_types, "Please enter a real shape")

if check_shape == "Triangle":

    triangle_outcome = input("What do you want to find (Area or Perimeter)? ")
    triangle_outcome_check = string_checker(triangle_outcome, ["area", "perimeter"], "This must be either Area or Perimeter")
    print()

    triangle_info = input("What do you know about the triangle (bh or abc)? ")
    triangle_info_check = string_checker(triangle_info, ["bh", "abc"], "Please say either 'bh' for base and height or abc for side lengths")
    triangle_calc = triangle(triangle_info_check, triangle_outcome)
    