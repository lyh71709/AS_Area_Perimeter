# Component 8 - Making a calculation history and print it at the end of the program
# Only put in triangles and rectangles

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

# get_shape function goes here
# get the desired shape
def get_shape():

    # Possible Shapes
    valid_shapes = [["square", "squ", "s"],
                    ["rectangle", "rec", "r"],
                    ["triangle", "tri", "t"],
                    ["circle", "cir", "c"],
                    ["parallelogram", "par", "p"],
                    ["trapezium", "tra", "t"]]

    valid = False
    while not valid:

        # Find the shape
        desired_shape = input("What shape do you want? ").lower()
        check_shape = string_checker(desired_shape, valid_shapes, "Please enter a real shape")

        # When invalid choice
        if check_shape == "invalid choice":
            continue
        # t can be either triangle or trapezium so ask to specify
        elif desired_shape == "t":
            print("Can you specify either triangle or trapezium\n")
            continue
        else:
            break

    return check_shape

# rectangle function goes here
# Find the base and height then calculate area and perimeter
def rectangle():
    valid = False
    while not valid:
        
        # Get base and height
        base = number_checker("What is the base? ", "Please enter a number above 0", float)
        height = number_checker("What is the height? ", "Please enter a number above 0", float)

        # ------------- Calculations -------------
        area = base * height
        perimeter = (2 * base) + (2 * height)

        # Check if it is a square
        if base == height:
            squ_or_rec = "square"
        else:
            squ_or_rec = "rectangle"

        # Print with appropriate shape name
        print("The area of your {} is {:.2f}".format(squ_or_rec, area))
        print("The perimeter of your {} is {:.2f}".format(squ_or_rec, perimeter))
        print()

        # return this until I put in a list for history
        return ["Rectangle", base, height, area, perimeter]

# triangle function goes here
# Figures out what the question gives and calculates the area and perimeter
def triangle():

    valid = False
    while not valid:

        # Find what the user is given
        info = input("What do you know about the triangle [Base and height(bh)] or [the side lengths(abc)]? ").lower()
        info_check = string_checker(info, [["bh"], ["abc"]], "Please say either 'bh' for base and height or 'abc' for side lengths")
        if info_check == "invalid choice":
            continue

        # ------------- Calculations -------------
        # If base and height is given
        if info_check == "Bh":

            # Find Base and height
            base = number_checker("What is the base? ", "Please enter a number bigger than 0", float)
            height = number_checker("What is the height? ", "Please enter a number bigger than 0", float)
                
            area = 0.5 * base * height
            perimeter = "couldn't find"

            print("The area of your triangle is {:.2f}".format(area))
            print("I can't find the perimeter with only base and height")

        # If triangle side lengths are given
        else:
            # Find triangle side lengths
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
history = []
calc_num = 0

keep_going = ""
while keep_going == "":
    what_shape = get_shape()

    if what_shape == "Rectangle":
            result = rectangle()
    else:
        result = triangle()

    history.append(result)
    keep_going = input("\nIf you want to continue press enter or any other key to quit: ")

print("==================== History ====================\n")
for item in history:
    calc_num += 1
    print("{}| Shape: {} | Area: {} | Perimeter: {}".format(calc_num, item[0], item[3], item[4]))
print()
    