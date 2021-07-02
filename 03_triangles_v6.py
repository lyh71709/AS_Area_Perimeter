# Component 3 - implementing triangles
# v2 - puts some required input fields in the function to shorten the main routine and implement the number checker in.
# v3 - change up some wording to make the program more usable
# v4 - doesn't ask for area or perimeter and just prints both
# v5 - solve the impossible triangle problem and change the return to make it history friendly
# v6 - make it unit friendly

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

# convert_unit function goes here
# Converts units and number appropriately according to what the user wants
def convert_unit(desired_unit, answer):
    # Set up lists to call, and have an index for units and all possible integers
    # The units are split up so that the spacing between the can determine the power of ten that they need to be mulitplied by
    unit_list = ["km", "", "", "m", "", "cm", "mm"]
    number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # This is when no unit at the back is given so it will autimatically assume that the unit is already in the desired unit form
    if answer[len(answer)-1] in number_list:
        # is the same as the number provided
        num = answer
        # unit is already in the form of desired unit
        unit = desired_unit
    # When the user has a put a specific unit at the back and is metres "m"
    # Checks this becasue all the units are two characters except for metres so I have to check this.
    else:
        # Finds the last character
        num = answer[:len(answer)-1]
        unit = answer[len(answer)-1]
        # If the unit is anything but metres "m"
        # Finds the second to last character and checks if it is not a number
        if answer[len(answer)-2] not in number_list:
            # Finds the second to last character
            num = answer[:len(answer)-2]
            unit = answer[len(answer)-2:]

    # Find the power that the unit conversion needs to be.
    index1 = unit_list.index(unit)
    index2 = unit_list.index(desired_unit)
    
    num = int(num)
    power = int(index2 - index1)

    converted_num = num*(10**power)
    # Return outcome (converted unit)
    return "{}{}".format(converted_num, desired_unit)


# triangle function goes here
# Figures out what the question gives and calculates the area and perimeter
def triangle(unit):

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
            converted_base = convert_unit(unit, base)
            converted_height = convert_unit(unit, height)

            print(converted_base)
            print(converted_height)
            recorded_info = ("Base: {} | Height: {}".format(base, height))
                
            area = 0.5 * base * height
            perimeter = "N/A"

            print("The area of your triangle is {:.2f}".format(area))
            print("I can't find the perimeter with only base and height")

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
                print("The area of your triangle is {:.2f}".format(area))
                print("The perimeter of your triangle is {:.2f}".format(perimeter))
            except ValueError:
                # When an impossible triangle is created
                print("The triangle you entered is a triangle that cannot exist")
                area = "N/A"
                perimeter = "N/A"

        # return this for use in history
        return ["Triangle", area, perimeter, recorded_info]


# Main Routine
# Set the shape as triangle to make testing easier seeing as how this is the triangle component
what_shape = "Triangle"
what_unit = input("Unit: ")

# Loop for testing purposes
for item in range(0,1):
    # Triangle Scenario
    if what_shape == "Triangle":
        result = triangle(what_unit)
    print()
