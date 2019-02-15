from check_number import check_num
from check_operator import check_op
from time import sleep

# Give number
# Give operator
# Give number 2
# Check numbers and operator
# Print the result
# Restart

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
                num = int(number)
                num2 = int(number2)
                result = num - num2
                print("Answer: " + str(result))
                i = 0
            elif operator == "+":
                num = int(number)
                num2 = int(number2)
                result = num + num2
                print("Answer: " + str(result))
                i = 0
            elif operator == "*":
                num = int(number)
                num2 = int(number2)
                result = num * num2
                print("Answer: " + str(result))
                i = 0
            elif operator == "/":
                num = int(number)
                num2 = int(number2)
                result = num / num2
                print("Answer: " + str(result))
                i = 0
            else:
                i = 1