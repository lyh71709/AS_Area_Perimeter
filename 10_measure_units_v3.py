# Nice to Have 1 - Units of Measurement
# Try to add a way of including units of measurement in the program
# v2 - Do this instead of brute force check
# v3 - Add another function to put rly big or rly small numbers in standard form

# convert_standard function goes here
# Converts integers/floats with greater than 6 digits to standard form
def convert_standard(num):
    # Finds the length of given integer/float
    length = len(str(num).replace('.',''))

    # Checks if length greater than 6 (can be changed)
    if length <= 6:
        return num
    else:
        # Writes number in standard form
        standard_num = format(num, "5.2e")
        return standard_num

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
    
    num = float(num)
    power = float(index2 - index1)

    converted_num = num*(10**power)
    standard_num = convert_standard(converted_num)
    num_with_unit = "{}{}".format(standard_num,desired_unit)

    # Return outcome (converted unit)
    return [converted_num, desired_unit, num_with_unit]
    
# Main Routine

what_unit = input("Unit: ")
length = input("Length: ")
conversion = convert_unit(what_unit, length)

print(conversion)