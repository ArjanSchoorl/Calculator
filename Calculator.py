def main():
    print("Calculator")
    while True:
        print()
        continu = input("Do you want to continue? Yes/No: ").lower()
        if continu == 'y' or continu == 'yes':
            result()
        else:
            print("Closing...")
            return False


def result():
    # Get all inputs to calculate
    num1 = input("Number one: ")
    operator = str(input("Operator (+-*/): "))
    num2 = input("Number two: ")

    if check_input(num1, num2, operator):
        calculate(num1, num2, operator)
        return True
    else:
        print("Input Error")
        return False


# This function checks if the val is a float or not
def check_input(num1, num2, operator):
    try:
        # Trying to get the float of val & val2
        float(num1)
        float(num2)
        if operator == "-":
            return True
        # Operator is addition
        elif operator == "+":
            return True
        # Operator is multiplication
        elif operator == "*":
            return True
        # Operator is division
        elif operator == "/":
            return True
        # Return True if val & val2 are floats
    except ValueError:
        # Return False if val & val2 are not floats
        return False


def calculate(num1, num2, operator):
    if operator == "-":
        # Get the result by subtracting number_2 from number_1
        # Then print the result
        result = float(num1) - float(num2)
        print(f"Answer: {str(result)}")
    elif operator == "+":
        # Get the result by addition number_1 and number_2
        # Then print the result
        result = float(num1) + float(num2)
        print(f"Answer: {str(result)}")
    elif operator == "*":
        # Get the result by multiplication number_1 with number_2
        # Then print the result
        result = float(num1) * float(num2)
        print(f"Answer: {str(result)}")
    elif operator == "/":
        # Get the result by division number_1 from number_2
        # Then print the result
        result = float(num1) / float(num2)
        print(f"Answer: {str(result)}")

main()