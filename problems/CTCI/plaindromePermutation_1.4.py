from collections import defaultdict

def plaindromePermutation(s):
    """
    itype : string
    rtype: true or false
    """
    # ind = [i-1 for i,j in enumerate(s) if i==" "] # searchiing for space
    l = len(s)
    tolerance = 1
    charMap = defaultdict(int) 
    
    for i in s.lower():
        if i!=" ":
            charMap[i] += 1
    print(charMap)
    for i in charMap.values():
        if tolerance >0:
            if i%2 != 0:
                tolerance-=1
        else:
            return False
    return True


if __name__ == "__main__":
    print(plaindromePermutation('Tact Coa'))
           