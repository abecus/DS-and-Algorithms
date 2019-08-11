

def minCost(costMat, m, n):
    dp = [[float('inf') for i in range(len(costMat))] for j in range(len(costMat[0]))]
    dp[0][0] = costMat[0][0]
  
    def helper(costMat, m, n):
        if dp[m][n]!=float('inf'):
            return dp[m][n]
        
        if n<0 or m<0:
            return float('inf')
        
        if m==0 and n==0:
            return dp[m][n]
        
        dp[m][n] = costMat[m][n] + min(helper(costMat, m-1, n-1), helper(costMat, m, n-1), helper(costMat, m-1, n))
        return dp[m][n]
    
    return helper(costMat, m, n), dp

cost = [[1, 2, 3], 
		[4, 8, 2], 
		[1, 5, 3]] 
print(minCost(cost, 2, 2)) 
