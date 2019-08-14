
def allPermutations(s):
    """
    itype: string
    rtype: None
    """
    d = {}
    def helper(s, p=[]):
        
        if s == []:
            p = ''.join(p)
            if p not in d:
                d[p] = 1
                print(p)
            return 
        
        for i in range(len(s)):
            # choose one letter
            temp = s[i]
            s.remove(temp)
            p.append(temp)
            
            helper(s, p)
            
            # unchoose letter
            s.insert(i, temp)
            p.remove(temp)
    
    return helper(s)
        
if __name__ == "__main__":
    a = 'abdulsalam'
    allPermutations([i for i in a])        
        