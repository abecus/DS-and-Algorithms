
def insertNext(num, l):
    for prime in l:
        if num % prime!=0:
            continue        
        else:
            break
    else:
        l.append(num)
    return l

def Primes(n):
    """
    itype: int
    rtype: list
    """
    l = [2]
    for i in range(3, n+1):
        insertNext(i, l)
    return l

print(Primes(11))
                
        
    