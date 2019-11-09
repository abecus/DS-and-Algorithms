import math
from itertools import product

def primeFactors(n, t): 
    l = set()
    l.add(1)
    # l.add(n)
    app = l.add
    while n % 2 == 0: 
        app(2)
        n = n/2
    for i in range(3,int(math.sqrt(t))+1,2): 
        while n % i== 0:
            app(i) 
            n = n / i 
    if n > 2: 
        app(n)
    return l




def divSum(num, t):
    l = set([1, num])
    t = min(t, int(num**0.5))
    i = 2
    while i<= t: 
        if (num % i == 0) : 
            if (i == (num / i)) : 
                l.add(i) 
            else : 
                l.add(i)
                l.add(num//i)
        i+=1
    return l
   
n, m = map(int, input().split())
t = min(n, m)
t1 = []
l = divSum(n, t)
g = divSum(m, t)
print(len(l.intersection(g)))

# 10 10 | 4
# 10 1 | 1
# 10 20 | 4
# 12345 12123 | 2
# 125 105 | 2
# 125 175 | 3
# 70 140 | 8

            