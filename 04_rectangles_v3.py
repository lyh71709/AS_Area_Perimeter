# Component 4 - implement rectangle function
# v2 - rename the print statement to square if the base == height
# v3 - make it history friendly and make it so that if square is put in user only needs a base

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

            # ------------- Calculations -------------
            area = base * height
            perimeter = (2 * base) + (2 * height)

        # Print with appropriate shape name
        print("The area of your {} is {:.2f}".format(squ_or_rec, area))
        print("The perimeter of your {} is {:.2f}".format(squ_or_rec, perimeter))
        print()

        # return this for use in history
        return ["Rectangle", area, perimeter, recorded_info]

# Main Routine

what_shape = "Rectangle"

# loop for testing purposes
for item in range(0,1):
    if what_shape == "Rectangle" or what_shape == "Square":
        result = rectangle()
