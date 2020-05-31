from collections import Counter
from functools import reduce
from math import sqrt, ceil
from operator import mul
from functools import lru_cache



def primeFactors_reduced(n): 
    gamma=1
    count=0
    while n % 2 == 0: 
        count += 1
        n = n//2
    gamma *= pow(2, ceil(count/2))
    
    for i in range(3, ceil(math.sqrt(n))+1, 2): 
        count = 0
        while n % i== 0:
            count += 1
            n = n // i 
        gamma *= pow(i, ceil(count/2))
              
    if n>2:
        gamma*=n
    return gamma
          
          
def primeFactor(n, factores):
    c=Counter()
    # if n in factores:   return  factores[n]
    while n%2==0:
        # if n in factores:   return factores[n]+c
        c[2]+=1
        n//=2
    for i in range(3, int(sqrt(n))+1, 2):
        # if n in factores:   return factores[n]+c
        while n%i==0:
            c[i]+=1
            n//=i
        if n==1:
            return c
    if n>2:
        c[n]+=1
    return c

def squaresLessThanUpper(fac, upper):
    facCopy = fac.copy()
    for el, p in facCopy.items():
        if p&1:
            facCopy[el]+=1

    val = reduce(mul, (i for i in facCopy.elements()))
    if val>upper:
        yield  upper, float('inf')
        return

    keys = tuple(sorted([*facCopy.keys()]))
    l=len(keys)

    @lru_cache(None)
    def helper(val):
        if val>upper:
            return
        else:
            yield val, sqrt(val)
            for i in range(l):
                facCopy[keys[i]]+=2
                val = reduce(mul, (i for i in facCopy.elements()))
                yield from helper(val)
                facCopy[keys[i]]-=2

    yield from helper(val)


def EratosthenesSieve(N):
    '''
    Calculating SPF (Smallest Prime Factor)
    for every number till N.
    Time Complexity : O(NloglogN)
    '''
    N+=1
    spf = [*range(N)]      # stores smallest prime factor for every number 
    
    # separately marking spf for every even number as 2 
    for i in range(4, N, 2):
        spf[i] = 2
    for i in range(3, ceil(sqrt(N))): 
        # checking if i is prime
        if (spf[i] == i):
            # marking SPF for all numbers divisible by i
            for j in range(i * i, N, i):
                # marking spf[j] if it is not previously marked 
                if (spf[j] == j):
                    spf[j] = i
    return spf
  
def getReducedFactorization(N, spf):
    '''
    A O(logN) function returning prime
    factorization by dividing by smallest
    prime factor at every step
    '''
    reduced = 1
    while (N!=1):
        prev=spf[N]
        c=0
        while spf[N]==prev:
            c+=1
            N//=spf[N]
        reduced*=pow(prev, ceil(c/2))
        prev=spf[N]
    return reduced


if __name__ == "__main__":
    n=100

    # print(sorted([*squaresLessThanUpper(primeFactor(n, {}), n*20)]))
    # print([(n*i, sqrt(n*i)) for i in range(1, 20) if (sqrt(n*i)//1)**2 == n*i])

    print(primeFactor(100, {}))
    print(primeFactor(420, {}))
    print(primeFactor(900, {}))
    N=10000
    spf=EratosthenesSieve(N)
    # print(spf)
    
    # x = 32
    # p = getReducedFactorization(x, spf)
    # print(p)
    print(primeFactors_reduced(100))
    print(primeFactors_reduced(420))
    print(primeFactors_reduced(900))
    # for i in range(len(p)): 
    #     print(p[i], end = " ") 