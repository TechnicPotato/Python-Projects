
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
#
