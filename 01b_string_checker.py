# Component 1a - make a string checker for the base component

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


# Main Routine
valid_names = [["henry"], ["aref"], ["jt"]]

# For loop for testing purposes
for item in range(0,4):

    name = input("Hello, what's your name? ").lower()
    name_check = string_checker(name, valid_names, "Please enter a real name")

    print(name_check)