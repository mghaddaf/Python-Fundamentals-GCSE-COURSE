again = input("Would you like to perform a calculation? Type 'yes' or 'no': ")
while again == "yes":
    number1 = int(input("Please type number 1: "))
    number2 = int(input("Please type number 2: "))
    operation = (input("Please type an operation: +, -, x, or /: "))
    if operation == "+":
        print(F"{number1} + {number2} = {number1 + number2}")
    if operation == "-":
        print(F"{number1} - {number2} = {number1 - number2}")
    if operation == "x":
        print(F"{number1} x {number2} = {number1 * number2}")
    if operation == "/":
        print(F"{number1} / {number2} = {number1 / number2}")
    again = input("Would you like to perform another calculation? Type 'yes' or 'no': ")
