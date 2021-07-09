# Component 2 - get the shape the user wants

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


# Main routine

what_shape = get_shape()

print("You chose {}".format(what_shape))