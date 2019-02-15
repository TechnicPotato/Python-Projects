
''' ------ Euler Projects ------ '''
#Basic file handling steps
'''fh =  open(r'C:\Users\w\Desktop\Programming\p022_names.txt')
toread = read(fh)'''
#Problem 22 T= 23:05
def p22():
    fh =  open(r'C:\Users\w\Desktop\Programming\p022_names.txt')
    toread = fh.read().replace('\"','').split(',')
    toread.sort()
    #64 minus
    return sum([(sum((ord(c) - 64) for c in name) * (toread.index(name) + 1)) for name in toread ])

#Problem 23 T = ~30 m +
def p23():
    abundant = [number for
                    number in range(1,28124-12)
                    if (number < sum([n for n in range(1,number//2 + 1) if (number % n == 0)]))]
    return abundant
    removelist =  [sum(a,b) for a in abundant for b in abundant if ((a + b) < 28124)]
    return removelist
'''On hold until a method for faster solving is determined'''

#Problem 24 T = 22:00
def p24():
    from itertools import permutations
    a = permutations([0,1,2,3,4,5,6,7,8,9])
    b = list(a)
    b.sort()
    return b[999999]

#Problem 25 T = 7:36
def fibonacci(terms):
    sequence = [1,1,2]
    if terms > 3:
        for i in range(2,terms - 1):
            if len(str(sequence[i] +sequence[i-1])) == 1000:
                break
            sequence.append(sequence[i] + sequence[i-1])

        return i + 2
    else:
        return False

#Problem 26 T =
'''On hold until I figure out a method'''

#Problem 28 T = 16:53
#Numbers in the grid = 1001*1001
#Grid moves by n//2 terms every (n-1)
def p28():
    from math import sqrt
    overallsum = 1
    n = (1001 * 1001)
    multiplier = 2
    last = 1
    #Find out how many sets of 4 are doable
    for i in range(1,(int(sqrt(n))//2)+1):
        overallsum += (4* last + 10* multiplier)
        last += 4*multiplier
        multiplier += 2
    return overallsum

#Problem 29 T = 5:19
def p29():
    l = []
    [l.append(a**b) for a in range(2,101) for b in range(2,101) if a**b not in l]
    return len(l)
