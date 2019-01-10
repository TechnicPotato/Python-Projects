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
        if operator == "+":
            result = float(operand1) + float(operand2)
            print(result)
        elif operator == "-":
            result = float(operand1) - float(operand2)
            print(result)
        elif operator == "*":
            result = float(operand1) * float(operand2)
            print(result)
        elif operator == "/":
            if float(operand2) == 0.0:
                print("Cannot divide by zero")
            else:
                result = float(operand1) / float(operand2)
                print(result)
        else:
            print("Invalid operator")

    else:
        print("Failed to input numbers")
else:
        if len(sys.argv) < 4:
            print("Insufficient parameters")
        else:
            print("Too many parameters")
