# Component 1a - make an integer checker for the base component

# Number checker function goes here
# Checks that it is not 0 and is a number
def number_checker(question, error, num_type):
    number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    valid = False
    while not valid:
        if num_type == "unit":
            response = (input(question)).lower()
            if response[len(response)-2] not in number_list:
                num = response[:len(response)-2]
            else:
                num = response[:len(response)-1]
            return num

        else:
            try:
                response = num_type(input(question))
            
                if response <= 0:
                    print(error)
                else:
                    return response

            except ValueError:
                print(error)

# Main Routine
height = number_checker("What is the height? ", "This must be a number and is more than 0", "unit")
base = number_checker("What is the base? ", "This must be a number and is more than 0", "unit")
print(base)
print(height)
area = height * base

print("{} x {} = {}".format(base, height, area))
print("The area is {}".format(area))