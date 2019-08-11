def tripleStepsRec(n):
    """
    recursive solution with space O(n) and time O(n)
    """
    dp  = [0,1,2,4]
    def helper(n):
        if n < len(dp):
            return dp[n]
        
        return helper(n-1)+helper(n-2)+helper(n-3)
    
    return helper(n)


def tripleStepsIter(n):
    a1 = 1
    a2 = 2
    a3 = 4
    
    for i in range(4, n+1):
        temp = a1+a2+a3
        a1 = a2
        a2, a3 = a3, temp       
                
    return a3
    
    
if __name__ == "__main__":
    print(tripleStepsRec(6))
    print(tripleStepsIter(6))