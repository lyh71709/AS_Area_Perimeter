# Component 9 - Add instructions to make code more usable

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

def instructions():
    print("========== Welcome to the Area and Perimeter Calcualtor ==========\n")
    print("HENRYB0T: Hello, My Name is HENRYB0T\n")
    
    valid = False
    while not valid:
        need_instructions = input("HENRYB0T: would you like me to show you the instructions? ")
        need_instructions_check = string_checker(need_instructions, [[["yes"],["y"]], [["no"],["n"]]], "Please Enter Yes or No")

        print(need_instructions_check)

        if need_instructions_check == "No":
            print("HENRYB0T: Fine")
            print("HENRYB0T: Have Fun, I will shut up now")
            break
        else:
            print("HENRYB0T: Okay then... \n"
                  "HENRYB0T: This program will calculate the area and perimeter of almost any shape you want.\n"
                  "              The available shapes are [Triangle, Rectangle, Circle, Parallelogram and Trapeziums.\n"
                  "              You can enter the first letter or the first three letters, for example `c` or `cir` for circle.\n"
                  "              Or you can jsut put in the whole name but remember to spell it correctly.")
            print("HENRYB0T: Depending on what shape you do I will need different types of information or else i can't do the\n"
                  "              calculations so make sure you have it.")

# Main Routine

have_instruction = instructions()