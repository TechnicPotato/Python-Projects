import sys
#Conditional attempt to determine if numbers are inputted
def conditions(a):
    try:
        float(a)
        return True
    except ValueError:
        return False

acceptablefunctions = ("+","-","*","/")

if len(sys.argv) == 4: #Sys.argv[0] returns file directory
    operand1 = sys.argv[1]
    operand2 = sys.argv[3]
    operator = sys.argv[2]
    if conditions(operand1) and conditions(operand2):
        f1 = float(operand1)
        f2 = float(operand2)
        validOperator == True
        dividebyZero == False
        if operator == "+":
            result = f1 + f2
        elif operator == "-":
            result = f1 - f2
        elif operator == "*":
            result = f1 * f2
        elif operator == "/":
            if f2 == 0.0:
                dividebyZero = True
            else:
                result = f1 / f2
        else:
            validOperator = False
        if validOperator == False:
            print("Invalid Operator")
        elif dividebyZero == True:
            print("Cannot divide by zero")
        else:
            print(result)

    else:
        print("Failed to input numbers")
else:
        if len(sys.argv) < 4:
            print("Insufficient parameters")
        else:
            print("Too many parameters")
