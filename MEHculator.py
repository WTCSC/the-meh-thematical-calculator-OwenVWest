import time
def verify_input_num(get):
    if get.isdigit():
        return(True)
    else:
        return(False)
def type_out(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
def multiply(x, y):
    return(x*y)
def divide(x, y):
    if y == 0:
        return 0
    else:
        return(x/y)
def add(x, y):
    return(x+y)
def subtract(x, y):
    return(x-y)
def power_of(x, y):
    main = x
    for i in range(1,y):
        main = main*x
    return(main)
calctype_ask = True
keep_calc = True
calctype = ""
type_out("Ugh, Well someone obviously cant do math. Welcome to the Meh-culator... \n")

while calctype_ask:
    type_out("Enter the first number: ")
    num1 = input()
    type_out("Enter the second...: ")
    num2 = input()
    while verify_input_num(num1) & verify_input_num(num2) == False:
        type_out("You didn't give me a number, you bothered opening a calculator and didn't give me a number to calculate... Try that again and do it right this time and DONT TYPE OUT THE NUMBER.\n")
        type_out("Enter the first number: ")
        num1 = input()
        type_out("Enter the second...: ")
        num2 = input()
    num1 = int(num1)
    num2 = int(num2)
    while keep_calc:
        ans = 0
        type_out("What calculation are you making me do?(+, -, /, *, ^): ")
        calctype = input()
        if calctype == "+":
            ans = add(num1, num2)
            keep_calc = False
            type_out(f"{num1} + {num2} is {ans}, Happy?\n")
        elif calctype == "-":
            ans = subtract(num1, num2)
            keep_calc = False
            type_out(f"{num1} - {num2} is {ans}, Happy?\n")
        elif calctype == "/":
            ans = divide(num1, num2)
            keep_calc = False
            type_out(f"{num1} / {num2} is {ans}, Happy?\n")
        elif calctype == "*":
            ans = multiply(num1, num2)
            keep_calc = False
            type_out(f"{num1} * {num2} is {ans}, Happy?\n")
        elif calctype == "^":
            ans = power_of(num1, num2)
            keep_calc = False
            type_out(f"{num1}^{num2} is {ans}, Happy?\n")
        else:
            type_out("You didnt give me a valid calculation type, use the listed characters that I GAVE YOU and try again.\n")
    type_out("Do you want me to do more calculations for you (please dont), Yes(Y) or No(N): ")
    cont_check = input("").lower()
    if cont_check == "y" or cont_check == "yes":
        calctype_ask = True
    elif cont_check == "n" or cont_check == "no":
        calctype_ask = False
    else:
        print("You didnt even answer the question how I asked you too, you cant even do a yes or no question correctly, seriously?")
        calctype_ask = False
