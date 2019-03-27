# P17 Project Euler
'''1. Define individual numbers
2. Define tens
3. Define 10-20
3. Define hundred, and use
4. Define thousand'''
numbers = ('one','two','three','four','five','six','seven','eight','nine')
tens = ('twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety')
weird = ('ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen')
hundred = 'hundred'
and_string = 'and'
thousand = 'thousand'

def conversion(s,n):
    length = len(n)
    if int(n) == 0:
        return print(s)      
    elif length == 1:
        s += numbers[int(n) - 1]
        n = '0'
        conversion(s,n)
    elif length == 2:
        if (int(n) < 20) and (int(n) >= 10):
            s += weird[int(n)-10]
            n = '0'
            conversion(s,n)
        else:
            s += tens[(int(n)//10) - 2] + ' '
            n = n[1]
            conversion(s,n)
    elif length == 3:
        s += (numbers[(int(n)//100) - 1] +" "+ hundred)
        n = str(int(n) - ((int(n)//100)*100))
        if n !='0':
            s +=" and "
            conversion(s,n)
        else:
            conversion(s,'0')
    elif length == 4:
        s = "one thousand"
        n = "0"
        conversion(s,n)
    else:
        print("Invalid")

while True:
    n = input("Enter number: ")
    if n == "Q":
        break
    else:
        conversion("",n)
    


