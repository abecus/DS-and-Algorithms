

def minCost(costMat, m, n):
    """
    finds the min cost form 0,0 coordinate to the given coordinate
    """
    dp = [[float('inf') for i in range(len(costMat))] for j in range(len(costMat[0]))]
    dp[0][0] = costMat[0][0]
  
    def helper(costMat, m, n):
        if dp[m][n]!=float('inf'):
            return dp[m][n]
        
        if n<0 or m<0:
            return float('inf')
        
        dp[m][n] = costMat[m][n] + min(helper(costMat, m-1, n-1), helper(costMat, m, n-1), helper(costMat, m-1, n))
        return dp[m][n]
    
    return helper(costMat, m, n), dp

cost = [[1, 2, 3], 
		[4, 8, 2], 
		[1, 5, 3]] 
print(minCost(cost, 2, 2)) 
