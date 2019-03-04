from time import sleep
import sys


# This function checks if the val is a float or not
def check_number(val, val2):
    try:
        # Trying to get the float of val & val2
        float(val)
        float(val2)
         # Return True if val & val2 are floats
        return True
    except ValueError:
        # Return False if val & val2 are not floats
        return False 


# This function checks what operator the value is
def check_operator(val):
    # Operator is subtraction
    if val == "-":
        return True
    # Operator is addition
    elif val == "+":
        return True
    # Operator is multiplication
    elif val == "*":
        return True
    # Operator is division
    elif val == "/":
        return True
    # val is not an operator? -> return False
    return False


# Declare state and print calculator
state = 0
print("Calculator")

# Start the calculator
while True:
    while state == 0:
        print("")
        number_1 = input("Number one: ")
        operator = str(input("Operator (+-*/): "))
        number_2 = input("Number two: ")
        state = 1

    while state == 1:
        if not check_number(number_1, number_2) or not check_operator(operator):
            print("There went something wrong!")
        else:
            if operator == "-":
                result = float(number_1) - float(number_2)
                print(f"Answer: {str(result)}")
            elif operator == "+":
                result = float(number_1) + float(number_2)
                print(f"Answer: {str(result)}")
            elif operator == "*":
                result = float(number_1) * float(number_2)
                print(f"Answer: {str(result)}")
            elif operator == "/":
                result = float(number_1) / float(number_2)
                print(f"Answer: {str(result)}")
            else:
                pass
        sleep(0.5)
        state = 0
