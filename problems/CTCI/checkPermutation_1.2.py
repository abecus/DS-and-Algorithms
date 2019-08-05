from collections import defaultdict

def checkPermutation(s1, s2):
    """
    itype : strings (s1, s2)
    rtype: true or false
    """
    if not len(s1)==len(s2):
        return False
        
    charcount = defaultdict(int)
    for i in s1:
        charcount[i] += 1
    
    for i in s2:
        if charcount[i] < 1:
            return False
        charcount[i] -= 1 
    
    return all([i==0  for i in charcount.values()])

if __name__ == "__main__":
    print(checkPermutation('abc', 'caj'))