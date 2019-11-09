"""
_________________________63. Unique Paths II_________________________
Difficulty: Medium		Likes: 1090		Dislikes: 181		Solution: Available
Total Accepted: 235.4K		Total Submission: 697.6K		Acceptance Rate: 33.8%
Tags:  Dynamic Programming, Array


A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.
Note: m and n will be at most 100.
Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

"""


def uniquePathsWithObstacles(obstacleGrid):
	from functools import lru_cache
	@lru_cache(None)
	def helper(r, c):
		if c==r==0:
			return 1
		elif c<0 or r<0 or obstacleGrid[r][c]==1:
			return 0
		return helper(r-1, c)+helper(r, c-1)
	a = helper(len(obstacleGrid)-1, len(obstacleGrid[0])-1)
	print(helper.cache_info())
	return a

if __name__ == "__main__":
	obstacleGrid = [[0,0,1],[0,0,0],[0,0,0]]
	print(uniquePathsWithObstacles(obstacleGrid,))


"""
similarQuestions::
		Unique Paths: Medium
		Unique Paths III: Hard
"""
