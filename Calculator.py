# This is the main function, here is where the magic happens
def main():
    # Print the title of this program
    print("Calculator")
    # Run program while it is True
    while True:
        print()
        # Get input from user to continue
        continu = input("Do you want to continue? Yes/No: ").lower()
        # If the input is yes/y continue with result()
        if continu == 'y' or continu == 'yes':
            result()
        # If the input is not yes/y close the program by return False
        else:
            print("Closing...")
            return False


# This function is the get all the inputs and to calculate the result
def result():
    # Get all inputs to calculate
    num1 = input("Number one: ")
    operator = str(input("Operator (+-*/): "))
    num2 = input("Number two: ")
    # Check if the inputs are a float or an operator
    if check_input(num1, num2, operator):
        # Calculate with the inputs and return True
        calculate(num1, num2, operator)
        return True
    # If inputs are not a float/operator then give an error and return False
    print("Input Error")
    return False


# This function checks if num1 and num2 is a float or not
# and checks if the operator is an operator
def check_input(num1, num2, operator):
    try:
        # Trying to get the float of num1 & num
        float(num1)
        float(num2)
        # If num1 and num2 are a float then it will check if operator is an operator and return True
        if operator == "-" or operator == "+" or operator == "*" or operator == "/":
            return True
    except ValueError:
        return False


# This function does the calculation with num1, num2 and the operator
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