from math import ceil, sqrt

def EratosthenesSieve(N:int)-> list:
    '''
    Calculating SPF (Smallest Prime Factor)
    for every number till N.
    Time Complexity : O(NloglogN)
    '''
    N+=1
    # stores smallest prime factor for every number
    spf = [*range(N)]
    
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


def getReducedFactorization(N:int, spf:list)-> int:
    """
    counts repetition of each prime from prime factorisation of N
    using trial method upon spf list, and calculating the ceil of 
    half of all prime's powers (pow(p, ceil(a/2))) and multiplying 
    them together.
    """
    gamma = 1
    while (N!=1):
        # keep a prime in prev variable
        prev=spf[N]
        # for counting the power
        c=0
        # counts power of a prime
        while spf[N]==prev:
            c+=1
            N//=spf[N]
        # multiplies the half ceil of power on primes
        gamma*=pow(prev, ceil(c/2))
        prev=spf[N]
    return gamma


def pythagoreanTriplets(n):
    # calculate spf array
    spf=EratosthenesSieve((n - int(sqrt((n<<1) -1)))<<1)
    # keeps the triplet count
    tripletCount=0
    # loopinf for every values of 2*b
    for b2 in range(4, (n - int(sqrt((n<<1) -1)))<<1, 2):
        # calculates reduced factor of 2*b
        gamma=getReducedFactorization(b2, spf)
        
        # for findin all triplets from 2*b
        for i in range(1, int(sqrt(b2*((b2>>1)-1)))//gamma+1):
            i*=gamma
            sqVal = i*i
            q=sqVal//b2
            # if z = q+i+(b2>>1) > n break else print triplet
            if q+i+(b2>>1)>n:
                break
            else:
                # remove comments in this else block to print Triplets
                x=q+i
                print((x, (b2>>1)+i, x+(b2>>1)))
                # tripletCount+=1
    return tripletCount


if __name__ == "__main__":
    n=100
    print(pythagoreanTriplets(n))