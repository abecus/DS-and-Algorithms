def generateNumber(n, base=2):
    """
    itype: int : number of digits in a number
    rtype: none
    
    It generates every possible numbers of a base <= 10 
    """
    
    def helper(n, base, prefix=""):
        # print(n)
        if n==0:
            print(prefix)
            return 
        else:
            for i in range(int(base)):
                helper(n-1, base, prefix=prefix+str(i))
        
    return helper(n, base=base, prefix ='')

generateNumber(2, base=3)