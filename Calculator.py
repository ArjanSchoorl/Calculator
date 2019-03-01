from time import sleep
import sys

# This function checks if the val is a float or not


def check_number(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

# This function checks what operator val is


def check_operator(val):
    if val == "-":
        return True
    elif val == "+":
        return True
    elif val == "*":
        return True
    elif val == "/":
        return True
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
        if not check_number(number_1):
            print("Number 'one' is not a number")
            sleep(1)
            state = 0
        elif not check_number(number_2):
            print("Number 'two' is not a number")
            sleep(1)
            state = 0
        elif not check_operator(operator):
            print("You did not use a operator")
            sleep(1)
            state = 0
        else:
            if operator == "-":
                print("Answer: " + str(float(number_1) - float(number_2)))
                state = 0
            elif operator == "+":
                print("Answer: " + str(float(number_1) + float(number_2)))
                state = 0
            elif operator == "*":
                print("Answer: " + str(float(number_1) * float(number_2)))
                state = 0
            elif operator == "/":
                print("Answer: " + str(float(number_1) / float(number_2)))
                state = 0
            else:
                print("Oops! There went something wrong!")
