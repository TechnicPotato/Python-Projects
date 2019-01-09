import sys
def conditions(a):
    try:
        float(a)
        return True
    except ValueError:
        return False

acceptablefunctions = ("+","-","*","/")

if len(sys.argv) == 4:
    if conditions(sys.argv[1]) and conditions(sys.argv[3]):
        if sys.argv[2] in acceptablefunctions:
            if sys.argv[2] == "/" and sys.argv[3] == "0":
                print("Cannot divide by zero")
            else:
                print(eval(sys.argv[1]+sys.argv[2]+sys.argv[3]))
        else:
            print("Invalid operator")
    else:
        print("Failed to input numbers")
else:
        if len(sys.argv) < 4:
            print("Insufficient parameters")
        else:
            print("Too many parameters")
