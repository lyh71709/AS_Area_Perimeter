
# Number checker function goes here
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