# Component 6 - implement trapezium function
# v2 - Fix a similar problem that parallelogram_v3 fixed and make it history friendly
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

# trapezium function goes here
# Find the base, height and side length then calculate area and perimeter
def trapezium():
    valid = False
    while not valid:

        # Find what the user is looking for
        info = string_checker("What do you want to find out [Area(a)] or [Perimeter(p)] or [Both(ap)]? ", [["a ", "a"], [" p", "p"], ["ap"]], " HENRYB0T: Please say either 'a' for area or 'p' for perimeter")
        
        # base is needed in all cases so it is outside the if statement
        base_a = number_checker("What is the first base? ", " HENRYB0T: Please enter a number above 0", float)
        base_b = number_checker("What is the second base? ", "Please enter a number above 0", float)
        # Check if user wants area
        if info[1] == "p" or info[1] == "P":
            side_c = number_checker("What is the first side length? ", " HENRYB0T: Please enter a number above 0", float)
            side_d = number_checker("What is the second side length? ", " HENRYB0T: Please enter a number above 0", float)
            # Check if user wants perimeter as well
            if info[0] == "A":
                height = number_checker("What is the height? ", " HENRYB0T: Please enter a number above 0", float)
                recorded_info = ("A: {} | B: {} | C: {} | D: {} | Height: {}".format(base_a, base_b, side_c, side_d, height))
            # If only area
            else:
                height = 0
                recorded_info = ("A: {} | B: {} | C: {} | D: {}".format(base_a, base_b, side_c, side_d))
        # Perimeter scenario
        else:
            height = number_checker("What is the height? ", " HENRYB0T: Please enter a number above 0", float)
            side_c = 0
            side_d = 0
            recorded_info = ("A: {} | B: {} | Height: {}".format(base_a, base_b, height))
        
        # ------------- Calculations -------------
        area = ((base_a + base_b)/2) * height
        perimeter = base_a + base_b + side_c + side_d

        # Area
        # Also ensures that area and perimeter is pluralised properly
        if height != 0:
            if area != 1:
                print("The area of your trapezium is {:.2f} units^2".format(area))
            else:
                print("The area of your trapezium is {:.2f} unit^2".format(area))
            # Perimeter as well
            if side_c != 0:
                if perimeter != 1:
                    print("The perimeter of your trapezium is {:.2f} units".format(perimeter))
                else:
                    print("The perimeter of your trapezium is {:.2f} unit".format(perimeter))
            else:
                perimeter = "N/A"
        # Perimeter only
        else:
            if perimeter != 1:
                print("The perimeter of your trapezium is {:.2f} units".format(perimeter))
            else:
                print("The perimeter of your trapezium is {:.2f} unit".format(perimeter))
            area = "N/A"
        print()
        # return this for use in history
        return ["Trapezium", area, perimeter, recorded_info]

# Main Routine

what_shape = "trapezium"

# Loop for testing purposes
for item in range(0,3):
    if what_shape == "trapezium":
        result = trapezium()
        