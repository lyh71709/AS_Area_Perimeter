# Component 1a - make a string checker for the base component
# same as the one for FRC
# v2 - altered so that the function asks the question as well

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

# Main Routine
valid_names = [["henry"], ["aref"], ["jt"]]

# For loop for testing purposes
for item in range(0,4):

    name_check = string_checker(("Hello, what's your name? ").lower(), valid_names, "Please enter a real name")

    print(name_check)