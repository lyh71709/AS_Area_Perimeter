# Component 3 - implementing triangles
# v2 - puts some required input fields in the function to shorten the main routine and implement the number checker in.
# v3 - change up some wording to make the program more usable
# v4 - doesn't ask for area or perimeter and just prints both
# v5 - solve the impossible triangle problem and change the return to make it history friendly
# v6 - Add in basic units and also use the more efficient string checker

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
def string_checker(question, options, error):
    valid = False
    while not valid:
        choice = input(question).lower()

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
            print()
            continue

# triangle function goes here
# Figures out what the question gives and calculates the area and perimeter
def triangle():

    valid = False
    while not valid:

        # Find what the user is given
        info = string_checker("What do you know about the triangle [Base and height(bh)] or [the side lengths(abc)]? ", [["bh"], ["abc"]], " HENRYB0T: Please say either 'bh' for base and height or 'abc' for side lengths")

        # ------------- Calculations -------------
        # If base and height is given
        if info == "Bh":

            # Find Base and height
            base = number_checker("What is the base? ", " HENRYB0T: Please enter a number bigger than 0", float)
            height = number_checker("What is the height? ", " HENRYB0T: Please enter a number bigger than 0", float)
            recorded_info = ("Base: {} | Height: {}".format(base, height))
                
            # Calculations
            area = 0.5 * base * height
            perimeter = "N/A"

            # Checks if the area isn't one
            if area != 1:
                # Plural
                print("The area of your triangle is {:.2f} units^2".format(area))
            else:
                # Non Plural
                print("The area of your triangle is {:.2f} unit^2".format(area))
            print(" HENRYB0T: I can't find the perimeter with only base and height")

        # If triangle side lengths are given
        else:
            # Find triangle side lengths
            a = number_checker("What is the length of a? ", "Please enter a number bigger than 0", float)
            b = number_checker("What is the length of b? ", "Please enter a number bigger than 0", float)
            c = number_checker("What is the length of c? ", "Please enter a number bigger than 0", float)
            recorded_info = ("A: {} | B: {} | C: {}".format(a, b, c))

            # Do Heron's Law and the sum of all the side lengths for perimeter
            s = (a + b + c) / 2
            perimeter = a + b + c

            # Try statement to take into account the impossible triangle problem and math error
            try:
                # When the math works
                area = math.sqrt(s * (s-a) * (s-b) * (s-c))
                # Checks if the area is not 1
                if area != 1:
                    print("The area of your triangle is {:.2f} units^2".format(area))     
                else:
                    print("The area of your triangle is {:.2f} unit^2".format(area))
                
                # Checks if perimeter is not 1
                if perimeter != 1:
                    print("The perimeter of your triangle is {:.2f} units".format(perimeter))
                else:
                    print("The perimeter of your triangle is {:.2f} unit".format(perimeter))
            except ValueError:
                # When an impossible triangle is created
                print(" HENRYB0T: The triangle you entered is a triangle that cannot exist")
                # Set to N/A so that the history will display N/A
                area = "N/A"
                perimeter = "N/A"

        # return this for use in history
        return ["Triangle", area, perimeter, recorded_info]


# Main Routine
# Set the shape as triangle to make testing easier seeing as how this is the triangle component
what_shape = "Triangle"

# Loop for testing purposes
for item in range(0,1):
    # Triangle Scenario
    if what_shape == "Triangle":
        result = triangle()
    print()
