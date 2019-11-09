"""
_________________________64. Minimum Path Sum_________________________
Difficulty: Medium		Likes: 1661		Dislikes: 43		Solution: Available
Total Accepted: 265.2K		Total Submission: 543.1K		Acceptance Rate: 48.8%
Tags:  Array, Dynamic Programming


Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""

from functools import lru_cache
def minPathSum(grid):
    r = len(grid)
    c = len(grid[0])

    @lru_cache(r*c)
    def helper(i, j, r=r, c=c):
        if i==0 and j==0:
            return grid[0][0]
        
        if i<0 or j<0:
            return float('inf')
        
        return grid[i][j]+min(helper(i-1, j),
                              helper(i, j-1))
    a = helper(r-1, c-1)
    # print(helper.cache_info())
    return a

if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    grid = [[1,2,3],
            [6,5,4],
            [8,7,9]]
    print(minPathSum(grid,))


"""
similarQuestions::
        Unique Paths: Medium
        Dungeon Game: Hard
        Cherry Pickup: Hard
"""
