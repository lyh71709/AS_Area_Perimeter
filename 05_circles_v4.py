# Component 5 - implement circles function
# v2 - I wasn't sure if I wanted to add in diameter but I did it anyway in v2 because I was 
#      worried that users who don't know that diameter is 2r won't be able to use the program
# v3 - Make it history friendly
# v4 - Make it say units and use more efficient string checker

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

# circle function goes here
# Find the radius or diameter then calculate area and circumference
def circle():
    valid = False
    while not valid:
        
        # Find what the user is given
        info = string_checker("What do you know about the circle [radius(r)] or [diameter(d)]? ", [["r"], ["d"]], "Please say either 'r' for radius or 'd' for diameter")

        # Diameter case
        if info == "D":
            diameter = number_checker("What is the diameter? ", "Please enter a number above 0", float)
            print(" HENRYB0T: Did You know that diameter is double the radius of the circle? So all you need to do to find the radius is hafl the diameter :)")
            # radius is diameter divided by 2
            r = diameter / 2
            recorded_info = ("Diameter: {}".format(diameter))
        # Radius Case
        else:
            radius = number_checker("What is the radius? ", "Please enter a number above 0", float)
            r = radius
        recorded_info = ("Radius: {}".format(r))

        # ------------- Calculations -------------
        circumference = 2 * (math.pi) * r
        area = (math.pi) * r**2

        if area != 1:
            print("The area of your circle is {:.2f} units^2".format(area))
        else:
            print("The area of your circle is {:.2f} unit^2".format(area))
        
        if circumference != 1:
            print("The circumference of your circle is {:.2f} units".format(circumference))
        else:
            print("The circumference of your circle is {:.2f} unit".format(circumference))
        print()

        # return this for use in history
        return ["Circle", area, circumference, recorded_info]

# Main Routine

what_shape = "circle"

for item in range(0,1):
    if what_shape == "circle":
        result = circle()
