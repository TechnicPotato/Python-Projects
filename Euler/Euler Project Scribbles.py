
''' ------ Euler Projects ------ '''
#Basic file handling steps
'''fh =  open(r'C:\Users\w\Desktop\Programming\p022_names.txt')
toread = read(fh)'''
from math import sqrt
#Problem 1
sum([x for x in range(1,1000) if (x % 5 == 0 or x % 3 == 0)])

#Problem 2 T = 10:00
def fibonacci(max):
    fibList = []
    a = 1
    b = 0
    c = None
    while (a < max):
        fibList.append(a)
        #Do the variable shift!
        c = b
        b = a
        a = b + c
    return fibList

sum(filter(lambda x: x%2 == 0,fibonacci(4000000)))

#Problem 3 T= 40:00
def recursive_division(n, list):
    for i in range(2,n + 1):
        if n % i  == 0:
            list.append(i)
            n = n // i
            if n == 1:
                return #break here
            else:
                recursive_division(n, list)
                break

def p3(n):
    primelist = []
    recursive_division(n,primelist)
    return primelist

#Problem 4 T = 5:54
def ispalindrome(n):
    return str(n)[::-1] == str(n)

max([a*b
    for a in range(100,1000)
        for b in range(100,1000)
            if ispalindrome(a * b)])

#Problem 5 T = 35:00
def p5(n):
    t = {}
    for i in range(1,n+1):
        t[i] = 0
    b = [c for c in range(2,n+1)]
    overallnum = map(lambda x: p3(x), b)
    for c in overallnum:
        temp = {}
        for i in c:
            if i in temp:
                temp[i] += 1
            else:
                temp[i] = 1
        for num in temp.keys():
            if temp[i] > t[i]:
                t[i] = temp[i]
    result = 1
    for i in t.keys():
        result *= i ** t[i]
    return result

#Problem 7 T = 13:24
def primes(target):
    primelist = [2]
    n = 3
    while len(primelist) < target:
        for prime in primelist:
            if n % prime == 0:
                n = n + 1
                break
        else:
            primelist.append(n)
            n = n + 1
    return primelist[target - 1]

#Problem 10
'''Find better sieve
def p10():
    primes = [2]
    for i in range(3,2000001):
        for prime in primes:
            if i%prime == 0:
                break
        else:
            primes.append(i)
    return sum(primes)'''

#Problem 11
def p11():
    fh = open(r"D:\Programming\input.txt")
    file = fh.read().split("\n")
    grid = [[int(a) for a in c.split(' ')] for c in file]
    horizontal = [grid[a][i]*grid[a][i+1]*grid[a][i+2]*grid[a][i+3]
                    for a in range(0,20)
                    for i in range(0,20-3)]
    rdiagonal = [grid[a][i]*grid[a+1][i+1]*grid[a+2][i+2]*grid[a+3][i+3]
                    for a in range(0,20-3)
                    for i in range(0,20-3)]
    ldiagonal = [grid[a][i]*grid[a+1][i-1]*grid[a+2][i-2]*grid[a+3][i-3]
                    for a in range(0,20-3)
                    for i in range(3,20)]
    vertical = [grid[a][i]*grid[a+1][i]*grid[a+2][i]*grid[a+3][i]
                    for a in range(0,20-3)
                    for i in range(0,20)]
    return max([max(vertical),max(horizontal),max(rdiagonal),max(ldiagonal)])

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
                    number in range(12,28124)
                    if (number < sum([n for n in range(1,number//2 + 1) if (number % n == 0)]))]
    returnlist = list(range(28124))
    for a in abundan
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
def fibonacci2(terms):
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

#Problem 30 T = 10:07
def p30():
    return [i for i in range(2,1000000) if sum([int(c)**5 for c in str(i)]) == i]
    #Potentially find a mathematical solution to a bounds for range()

#Problem 34 T =
def fact(n):
    return [n-1 * ]

#Problem 48 T = 2:19
def p48():
    output = []
    for i in range(1,1001):
        output.append(i**i)
    a = str(sum(output))
    return a[len(a)-10:len(a)]


