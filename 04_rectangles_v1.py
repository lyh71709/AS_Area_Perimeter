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
        return ""

# Main Routine

what_shape = "Rectangle"

# loop for testing purposes
for item in range(0,1):
    if what_shape == "Rectangle" or what_shape == "Square":
        result = rectangle()
