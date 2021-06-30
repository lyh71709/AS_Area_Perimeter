# Nice to Have 1 - Units of Measurement
# Try to add a way of including units of measurement in the program

def convert_unit(desired_unit, answer):

    if desired_unit == "m":
        measurement_unit = answer[len(answer) - 2:]
        num = int(answer[:len(answer)-2])

        if measurement_unit == "cm":
            new_num = "{:.2f}".format(num / 100)    
        elif measurement_unit == "mm":
            new_num = "{:.3f}".format(num /1000)
        else:
            new_num = "{}".format(num * 1000)
        return "{}{}".format(new_num, desired_unit)
        
    else:
        return "nope"

# Main Routine
what_unit = input("What unit of measurement do you want? ").lower()
length = input("What is the length? ")
converted_unit = convert_unit(what_unit, length)

print(converted_unit)
