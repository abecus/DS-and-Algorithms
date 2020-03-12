"""
_________________________1260. Shift 2D Grid_________________________
Difficulty: Easy		Likes: 104		Dislikes: 62		Solution: Available
Total Accepted: 10.2K		Total Submission: 16.8K		Acceptance Rate: 60.4%
Tags:  Array


Given a 2D grid of size m x n and an integer k. You need to shift
the grid k times. In one shift operation:  Element at grid[i][j]
moves to grid[i][j + 1]. Element at grid[i][n - 1] moves to grid[i
+ 1][0]. Element at grid[m - 1][n - 1] moves to grid[0][0]. 
Return the 2D grid after applying shift operation k times.   


Example 1:Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]

Example 2:Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]
 m == grid.lengthn == grid[i].length1 <= m <= 501 <= n <= 50-1000 <= grid[i][j] <= 10000 <= k <= 100
"""


def shiftGrid(grid, k):	
	for _ in range(k%(len(grid[0])*len(grid))):
		for row in range(len(grid)):
			for col in reversed(range(len(grid[0])-1)):
				grid[row][col+1], grid[row][col] = grid[row][col], grid[row][col+1]

		for row in reversed(range(len(grid)-1)):
			grid[row+1][0], grid[row][0] = grid[row][0], grid[row+1][0]
	return grid




if __name__ == "__main__":
	grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
	k = 4
	print(shiftGrid(grid,k,))


"""
"""
