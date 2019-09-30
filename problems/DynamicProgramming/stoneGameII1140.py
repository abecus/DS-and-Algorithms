"""
_________________________1140. Stone Game II_________________________
Difficulty: Medium		Likes: 124		Dislikes: 28		Solution: None
Total Accepted: 4.7K		Total Submission: 7.8K		Acceptance Rate: 60.0%
Tags:  Dynamic Programming


Alex�and Lee continue their�games with piles of stones.� There are a number of�piles�arranged in a row, and each pile has a positive integer number of stones�piles[i].� The objective of the game is to end with the most�stones.�
Alex and Lee take turns, with Alex starting first.� Initially, M = 1.
On each player's turn, that player�can take all the stones in the first X remaining piles, where 1 <= X <= 2M.� Then, we set�M = max(M, X).
The game continues until all the stones have been taken.
Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.

Example 1:


Input: piles = [2,7,9,4,4]

Output: 10

Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 

Constraints:

1 <= piles.length <= 100
1 <= piles[i]�<= 10 ^ 4
"""

from functools import lru_cache
def stoneGameII(piles):
        n = len(piles)
        dp = [[0]*n for _ in range(n)]
        for i in range(n-2,-1,-1):
            piles[i] += piles[i+1]

        @lru_cache(None)
        def dp(i,m):
            if i+2*m >= n:
                return piles[i]
            return piles[i] - min(dp(i+x,max(m,x)) for x in range(1,2*m+1))
        # return dp(0, 1)    
        
        # for i in range(n-1,-1,-1):
        #     for m in range(n-1,0,-1):
        #         # print(i ,m, piles[i])
        #         dp[i][m] = piles[i]
        #         if i + 2*m < n:
        #             # print('\t', i, m)
        #             # print('\t\t', [dp[i+x][max(m,x)] for x in range(1,2*m+1)])
        #             dp[i][m] -= min(dp[i+x][max(m,x)] for x in range(1,2*m+1))
        # return dp[0][1]

if __name__ == "__main__":
	piles = [2,7,9,4,4]
	print(stoneGameII(piles,))

