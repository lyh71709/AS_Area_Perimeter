# Area And Perimeter Base Code
# v2 - implement os and clear to make the  look cleaner
# v3 - implement units of measurements

import math
import pandas
import os


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


# get_shape function goes here
# get the desired shape
def get_shape():

    # Possible Shapes
    valid_shapes = [["square", "squ", "s"],
                    ["rectangle", "rec", "r"],
                    ["triangle", "tri"],
                    ["circle", "cir", "c"],
                    ["parallelogram", "par", "p"],
                    ["trapezium", "tra"]]

    # Find the shape
    desired_shape = string_checker("What shape do you want? ", valid_shapes, "Please enter a real shape or specify your shape")

    return desired_shape


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


# rectangle function goes here
# Find the base and height then calculate area and perimeter
def rectangle(squ_or_rec):
    valid = False
    while not valid:
        
        # Finds out if the user wanted a square or not
        # If so then only ask for a base
        if squ_or_rec == "Square":
            base = number_checker("What is the base? ", "Please enter a number above 0", float)
            recorded_info = ("Base: {}".format(base))

            # ------------- Calculations -------------
            area = base**2
            perimeter = base*4
        # If user wants a rectangle
        else:
            # Get base and height
            base = number_checker("What is the base? ", "Please enter a number above 0", float)
            height = number_checker("What is the height? ", "Please enter a number above 0", float)
            recorded_info = ("Base: {} | Height: {}".format(base, height))
            if base == height:
                print("HENRYB0T: Um that is actually a square :|\n")
                squ_or_rec = "Square"

            # ------------- Calculations -------------
            area = base * height
            perimeter = (2 * base) + (2 * height)

        # Print with appropriate shape name
        # Checks for pluralisation
        if area != 1:
            print("The area of your {} is {:.2f} units^2".format(squ_or_rec, area))
        else:
            print("The area of your {} is {:.2f} unit^2".format(squ_or_rec, area))

        if perimeter != 1:
            print("The perimeter of your {} is {:.2f} units".format(squ_or_rec, perimeter))
        else:
            print("The perimeter of your {} is {:.2f} unit".format(squ_or_rec, perimeter))
        print()

        # return this for use in history
        return ["Rectangle", area, perimeter, recorded_info]

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
        return ["Circle", "{:.2f}".format(area), "{:.2f}".format(circumference), recorded_info]


# parallelogram function goes here
# Find the base, height and side length then calculate area and perimeter
def parallelogram():
    valid = False
    while not valid:

        # Find what the user is looking for
        info = string_checker("What do you want to find out [Area(a)] or [Perimeter(p)] or [Both(ap)]? ", [["a ", "a"], [" p", "p"], ["ap"]], "Please say either 'a' for area or 'p' for perimeter")
        
        # base is needed in all cases so it is outside the if statement
        base = number_checker("What is the base? ", "Please enter a number above 0", float)
        # Check if user wants area
        if info[0] == "A":
            height = number_checker("What is the height? ", "Please enter a number above 0", float)
            # Check if user wants perimeter as well
            if info[1] == "p":
                side = number_checker("What is the side length? ", "Please enter a number above 0", float)
                recorded_info = ("Base: {} | Height: {} | Side: {}".format(base, height, side))
            # If only area
            else:
                side = 0
                recorded_info = ("Base: {} | Height: {}".format(base, height))
        # Perimeter scenario
        else:
            side = number_checker("What is the side length? ", "Please enter a number above 0", float)
            height = 0
            recorded_info = ("Base: {} | Side: {}".format(base, side))
        
        # ------------- Calculations -------------
        area = base * height
        perimeter = 2 * (side + base)

        # Area
        if height != 0:
            if area != 1:
                print("The area of your parallelogram is {:.2f} units^2".format(area))
            else:
                print("The area of your parallelogram is {:.2f} unit^2".format(area))
            # Perimeter as well
            if side != 0:
                if perimeter != 1:
                    print("The perimeter of your parallelogram is {:.2f} units".format(perimeter))
                else:
                    print("The perimeter of your parallelogram is {:.2f} unit".format(perimeter))
            else:
                perimeter = "N/A"
        # Perimeter only
        else:
            if perimeter != 1:
                print("The perimeter of your parallelogram is {:.2f} units".format(perimeter))
            else:
                print("The perimeter of your parallelogram is {:.2f} unit".format(perimeter))
            area = "N/A"
        print()
        # return this for use in history
        return ["Parallelogram", area, perimeter, recorded_info]

# trapezium function goes here
# Find the base, height and side length then calculate area and perimeter
def trapezium():
    valid = False
    while not valid:

        # Find what the user is looking for
        info = string_checker("What do you want to find out [Area(a)] or [Perimeter(p)] or [Both(ap)]? ", [["a ", "a"], [" p", "p"], ["ap"]], "Please say either 'a' for area or 'p' for perimeter")
        
        # base is needed in all cases so it is outside the if statement
        base_a = number_checker("What is the first base? ", "Please enter a number above 0", float)
        base_b = number_checker("What is the second base? ", "Please enter a number above 0", float)
        # Check if user wants area
        if info[1] == "p" or info[1] == "P":
            side_c = number_checker("What is the first side length? ", "Please enter a number above 0", float)
            side_d = number_checker("What is the second side length? ", "Please enter a number above 0", float)
            # Check if user wants perimeter as well
            if info[0] == "A":
                height = number_checker("What is the height? ", "Please enter a number above 0", float)
                recorded_info = ("A: {} | B: {} | C: {} | D: {} | Height: {}".format(base_a, base_b, side_c, side_d, height))
            # If only area
            else:
                height = 0
                recorded_info = ("A: {} | B: {} | C: {} | D: {}".format(base_a, base_b, side_c, side_d))
        # Perimeter scenario
        else:
            height = number_checker("What is the height? ", "Please enter a number above 0", float)
            side_c = 0
            side_d = 0
            recorded_info = ("A: {} | B: {} | Height: {}".format(base_a, base_b, height))
        
        # ------------- Calculations -------------
        area = ((base_a + base_b)/2) * height
        perimeter = base_a + base_b + side_c + side_d

        # Area
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


# instructions funtion goes here
# Asks if user wants instructions then print accordingly
def instructions():
    # Title
    print("========== Welcome to the Area and Perimeter Calculator ==========\n")
    print(" HENRYB0T: Hello, My Name is HENRYB0T\n")

    # Ask if user wants the instructions
    valid = False
    while not valid:
        need_instructions = string_checker(" HENRYB0T: Would you like me to show you the instructions? ", [["yes","y"], ["no","n"]], " HENRYB0T: Please Enter Yes or No\n")

        # No scenario
        if need_instructions == "No":
            print(" HENRYB0T: Fine")
        # Yes scenario
        else:
            print(" HENRYB0T: Okay then...\n\n"
                  " HENRYB0T: This program will calculate the area and perimeter of almost any shape you want.\n"
                  "            The available shapes are [Triangle, Square, Rectangle, Circle, Parallelogram and Trapeziums.\n"
                  "            You can enter the first letter or the first three letters, for example 'c' or 'cir' for circle.\n"
                  "            or you can jsut put in the whole name but remember to spell it correctly.\n"
                  "            *Please note that 't' will not work because it can be either triangle or trapezium so go more in depth for those. :)")
            print(" HENRYB0T: Depending on what shape you do I will need different types of information or else I can't do the\n"
                  "            calculations so make sure you have it.")
            print(" HENRYB0T: After a calculation the program will ask if you want to keep going, so just press enter if you do \n"
                  "            or put in any key then enter to stop. After you have stopped the code will print out a table of your calculations \n"
                  "            so you can go over them again.")
            print(" HENRYB0T: Remember to not use this program to cheat in any test and use it only for education purposes. :)")
        print(" HENRYB0T: Enjoy the program and get calculating!\n" 
              " HENRYB0T: Have Fun, I will shut up now\n")
        # Return nothing because nothing is needed
        return ""


# Main Routine
history = []

# Clears the terminal
clear = lambda:os.system('cls')
clear()

# Begins intstructions
have_instruction = instructions()

# Whole main routine loop
keep_going = ""
while keep_going == "":
    # Get user's desired shape
    what_shape = get_shape()

    # Checks if it is a Triangle
    if what_shape == "Triangle":
        result = triangle()
    # Checks if it is a rectangle or square
    elif what_shape == "Rectangle" or what_shape == "Square":
        result = rectangle(what_shape)
    # Checks if it is a circle
    elif what_shape == "Circle":
        result = circle()
    # Checks if it is a parallelogram
    elif what_shape == "Parallelogram":
        result = parallelogram()
    # Checks if it is a trapezium
    else:
        result = trapezium()

    # Append the results to a list for putting in a dataframe
    history.append(result)
    # Exit Loop or loop again
    keep_going = input("\nIf you want to continue press enter or any other key to quit: ")

# Puts results in a dataframe
print()
print("=============== History ===============\n")
history_frame = pandas.DataFrame(history, columns=["Shape", "Area", "Perimeter", "Info"])

# Print Dataframe
print(history_frame)
