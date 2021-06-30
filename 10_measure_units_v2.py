# Nice to Have 1 - Units of Measurement
# Try to add a way of including units of measurement in the program

def convert_unit(desired_unit, answer):
    unit_list = ["km", "", "", "m", "", "cm", "mm"]
    number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    num = answer[:len(answer)-1]
    unit = answer[len(answer)-1]
    if num not in number_list:
        num = answer[:len(answer)-2]
        unit = answer[len(answer)-2:]

    index1 = unit_list.index(unit)
    index2 = unit_list.index(desired_unit)
    
    num = int(num)
    power = int(index2 - index1)

    converted_num = num*(10**power)
    return "{}{}".format(converted_num, desired_unit)
    
# Main Routine

what_unit = input("Unit: ")
length = input("Length: ")
conversion = convert_unit(what_unit, length)

print(conversion)