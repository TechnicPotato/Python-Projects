
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

#Problem 24 T = 22:00
def p24():
    from itertools import permutations
    a = permutations([0,1,2,3,4,5,6,7,8,9])
    b = list(a)
    b.sort()
    return b[999999]
