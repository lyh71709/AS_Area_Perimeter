# Component 6 - implement parallelogram function
# v2 - The previous component was just a basic three if conditions and then ask accordingly
#      But I prefer this method because personally even though it might basically be the same length it is more clean and neat.
# v3 - Found a problem where the function finds both area and perimeter regardless of what the user wants and make the return statement able for history
# v4 - Make it say units and use more efficient string checker

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

# parallelogram function goes here
# Find the base, height and side length then calculate area and perimeter
def parallelogram():
    valid = False
    while not valid:

        # Find what the user is looking for
        info = string_checker("What do you want to find out [Area(a)] or [Perimeter(p)] or [Both(ap)]? ", [["a ", "a"], [" p", "p"], ["ap"]], " HENRYB0T: Please say either 'a' for area or 'p' for perimeter")
        
        # base is needed in all cases so it is outside the if statement
        base = number_checker("What is the base? ", " HENRYB0T: Please enter a number above 0", float)
        # Check if user wants area
        if info[0] == "A":
            height = number_checker("What is the height? ", " HENRYB0T: Please enter a number above 0", float)
            # Check if user wants perimeter as well
            if info[1] == "p":
                side = number_checker("What is the side length? ", " HENRYB0T: Please enter a number above 0", float)
                recorded_info = ("Base: {} | Height: {} | Side: {}".format(base, height, side))
            # If only area
            else:
                side = 0
                recorded_info = ("Base: {} | Height: {}".format(base, height))
        # Perimeter scenario
        else:
            side = number_checker("What is the side length? ", " HENRYB0T: Please enter a number above 0", float)
            height = 0
            recorded_info = ("Base: {} | Side: {}".format(base, side))
        
        # ------------- Calculations -------------
        area = base * height
        perimeter = 2 * (side + base)

        # Area
        # Also ensures that area and perimeter is pluralised properly
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

# Main Routine

what_shape = "parallelogram"

# Loop for testing purposes
for item in range(0,3):
    if what_shape == "parallelogram":
        result = parallelogram()
