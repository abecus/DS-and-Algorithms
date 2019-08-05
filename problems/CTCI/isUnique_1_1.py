from collections import defaultdict

def isUnique(s):
    """
    itype : string
    rtype: true or false
    """
    charMap = defaultdict(int)
    for i in s:
        if charMap[i] == 1:
            return False
        charMap[i] += 1
    return True        
    
    
if __name__ == "__main__":
    print(isUnique('abdd'))