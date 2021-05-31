# Component 1a - make a string checker for the base component

# string_checker function goes here
# Ensures that an input is within the possible results
def string_checker(choice, options, error):
    for var_list in options:

        # if the snack is in one of the lists, return the full list
        if choice in var_list:

            # Get full name of snack and put it in title case
            # so it looks nice when out putted
            chosen = choice.title()
            is_valid = "yes"
            break

        # if the chosen snack is not valid, set snack_ok to no
        else:
            is_valid = "no"

    # If snack is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        print(error + "\n")
        return "invalid choice"

# Main Routine
shape_types = ["square", "rectangle", "parallelogram", "triangle", "circle", "trapezium"]

what_shape = input("What shape do you want? ")
check_shape = string_checker(what_shape, shape_types, "Please enter a real shape")

print(check_shape)