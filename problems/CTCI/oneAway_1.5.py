"""
one way is to do sorting making time{O(NlogN)} and space{O(1)}

But i'm doing it using hashyable or dictionary making
time{O(N)}, space{O(1)} (because their are only 26 charecters 
in english alphabets)
"""
from collections import defaultdict

def oneAway(s1, s2):
    """
    itype : s1(string), s2(string)
    rtype: True, False
    """
    charcount = defaultdict(int)
    tolerance = 1
    
    for i in s1.lower():
        charcount[i] += 1
    
    for i in s2.lower():
        if tolerance>0:
            if i not in charcount:
                tolerance -=1
                
            else:
                if charcount[i]>0:
                    charcount[i] -=1
                    
                else:
                    return False
        else:
            return False
    print(charcount)
    return True


if __name__ == "__main__":
    
    s1 = 'pale'
    s2 = 'bake'
    print(oneAway(s1, s2))
        