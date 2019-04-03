# 20 * 20 Grid
'''2 choices right or down
must go 20 right and 20 down
if it hits the end, must force right
if it hits the right, must force down
program must make 1 of 2 choices, 40 times.
default to A hit
if cannot hit A, hit B
'''
overall = []
while True:
    current = ""
    if len(current) == 40:
        if current in overall:
            break
        else:
            overall.append(current)
    elif current.count("A") == 20:
        current += "B"
    elif current.count("B") == 20:
        current += "A"
    elif (current + "A") in overall:
        
    
