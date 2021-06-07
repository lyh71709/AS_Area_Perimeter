# Component 2 - get the shape the user wants

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

        if check_shape == "invalid choice":
            continue
        elif desired_shape == "t":
            print("Can you specify either triangle or trapezium\n")
            continue
        else:
            break

    return check_shape

# string_checker function goes here
# Ensures that an input is within the possible results
def string_checker(choice, options, error):
    for var_list in options:

        # if the shape is in one of the lists, return the full list
        if choice in var_list:

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
        print(error + "\n")
        return "invalid choice"


# Main routine

what_shape = get_shape()

print("You chose {}".format(what_shape))