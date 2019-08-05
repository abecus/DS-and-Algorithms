def pairsBoutforce(x):
    # O(n^4) time complexity
    # O(1) space complexity
    for a in range(1,x):
        for b in range(1, x):
          for c in range(1, x):
            for d in range(1, x):
                if a**3+b**3==c**3+d**3:
                    yield (a,b,c,d)

def pairsOptimised(x):
    # O(n^2) time complexity
    # O(n) space complexity
    l = {}
    for a in range(1, x):
        for b in range(1, x):
            result = a**3+b**3
            l[result] = (a, b)
            
    for pairs in l.values():
        if pairs[0] != pairs[1]:
            yield f'{(pairs[0], pairs[1], pairs[0], pairs[1])}\n{(pairs[0], pairs[1], pairs[1], pairs[0])}'
        else:
            yield (pairs[0], pairs[1], pairs[0], pairs[1])
        
                    
for i in pairsOptimised(10):
    print(i)