# Nice to Have 1 - Units of Measurement
# Try to add a way of including units of measurement in the program
# v2 - Do this instead of brute force check


# convert_unit function goes here
# Converts units and number appropriately according to what the user wants
def convert_unit(desired_unit, answer):
    # Set up lists to call, and have an index for units and all possible integers
    # The units are split up so that the spacing between the can determine the power of ten that they need to be mulitplied by
    unit_list = ["km", "", "", "m", "", "cm", "mm"]
    number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # This is when no unit at the back is given so it will autimatically assume that the unit is already in the desired unit form
    if answer[len(answer)-1] in number_list:
        # is the same as the number provided
        num = answer
        # unit is already in the form of desired unit
        unit = desired_unit
    # When the user has a put a specific unit at the back and is metres "m"
    # Checks this becasue all the units are two characters except for metres so I have to check this.
    else:
        # Finds the last character
        num = answer[:len(answer)-1]
        unit = answer[len(answer)-1]
        # If the unit is anything but metres "m"
        # Finds the second to last character and checks if it is not a number
        if answer[len(answer)-2] not in number_list:
            # Finds the second to last character
            num = answer[:len(answer)-2]
            unit = answer[len(answer)-2:]

    # Find the power that the unit conversion needs to be.
    index1 = unit_list.index(unit)
    index2 = unit_list.index(desired_unit)
    
    num = int(num)
    power = int(index2 - index1)

    converted_num = num*(10**power)
    # Return outcome (converted unit)
    return "{}{}".format(converted_num, desired_unit)
    
# Main Routine

what_unit = input("Unit: ")
length = input("Length: ")
conversion = convert_unit(what_unit, length)

print(conversion)