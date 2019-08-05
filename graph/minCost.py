# from functools import lru_cache


# @lru_cache(maxsize=128)
def minCost(costMat, m, n):
    print(m,n)
    if m==0 or n==0:
        return costMat[m][n]
    return min(minCost(costMat, m-1, n-1), minCost(costMat, m, n-1), minCost(costMat, m-1, n)) + costMat[m][n]

cost = [[1, 2, 3], 
		[4, 8, 2], 
		[1, 5, 3]] 
print(minCost(cost, 2, 2))
# print(cost[0][0]) 
