from time import sleep
import sys

# This is a test
# Give number
# Give operator
# Give number 2
# Check numbers and operator
# Print the result
# Restart

def check_num(val):
    try:
        float(val)
        return True
    except ValueError:
        return False


def check_op(val):
    if val == "-":
        return True
    elif val == "+":
        return True
    elif val == "*":
        return True
    elif val == "/":
        return True
    else:
        return False

def user_restart():
    answer = input("Continue? Yes or No: ").lower()
    if answer == "yes" or answer == "y":
        return True
    else:
        print("Thank you for using this calculator!")
        return False


i = 0
print("Calculator")

while True:
    while i == 0:
        print("")
        number = input("Number one: ")
        operator = str(input("Operator (+-*/): "))
        number2 = input("Number two: ")
        i = 1

    while i == 1:
        if not check_num(number):
            print("Number 'one' is not a number")
            sleep(1)
            i = 0
        elif not check_num(number2):
            print("Number 'two' is not a number")
            sleep(1)
            i = 0
        elif not check_op(operator):
            print("You did not use a operator")
            sleep(1)
            i = 0
        else:
            if operator == "-":
                num = float(number)
                num2 = float(number2)
                result = num - num2
                print("Answer: " + str(result))
                if user_restart():
                    i = 0
                else:
                    sys.exit()
            elif operator == "+":
                num = float(number)
                num2 = float(number2)
                result = num + num2
                print("Answer: " + str(result))
                if user_restart():
                    i = 0
                else:
                    sys.exit()
            elif operator == "*":
                num = float(number)
                num2 = float(number2)
                result = num * num2
                print("Answer: " + str(result))
                if user_restart():
                    i = 0
                else:
                    sys.exit()
            elif operator == "/":
                num = float(number)
                num2 = float(number2)
                result = num / num2
                print("Answer: " + str(result))
                if user_restart():
                    i = 0
                else:
                    sys.exit()
            else:
                sys.exit()