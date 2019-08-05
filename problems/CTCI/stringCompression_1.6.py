def stringCompression(s):
    """
    itype : str
    rtype: str
    """        

    l = []
    count = 1
    temp = s[0]
    
    for i in range(1, len(s)):
        if s[i] == temp:
            count +=1
            continue
        
        l += [s[i-1], str(count)]
        count = 1
        temp = s[i]
        
    l += [s[i-1], str(count)]
    l = ''.join(l)
    
    return l if len(l)<len(s) else s
          

if __name__ == "__main__":
    
    s = 'aabccccaaa'
    s2 = 'aabcddefghii'
    print(stringCompression(s2))