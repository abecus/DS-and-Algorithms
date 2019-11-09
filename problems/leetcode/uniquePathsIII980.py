"""
_________________________980. Unique Paths III_________________________
Difficulty: Hard		Likes: 310		Dislikes: 42		Solution: Available
Total Accepted: 17.9K		Total Submission: 25.1K		Acceptance Rate: 71.6%
Tags:  Backtracking, Depth-first Search


On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.
 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation:
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.




 
Note:

1 <= grid.length * grid[0].length <= 20
"""

count = 0
def uniquePathsIII(grid):
	tr = [1,0,-1,0]
	tc = [0,1,0,-1]

	def canGo(r, c):
		if not(0<=r<l and 0<=c<m) or\
			grid[r][c]==-1 or grid[r][c]==3 or\
			grid[r][c]==1 or grid[r][c]==2:
			return 0
		return 1

	def canReach2(r, c):
     
		for i,j in zip(tr,tc):
			row=r+i
			col=c+j
			if (0<=row<l and 0<=col<m) and grid[r+i][c+j]==2:
				return 1
		return 0
 
	def solve(r,c,zeros):
		global count
		if zeros==0 and canReach2(r, c):
			count+=1
			return
		for i,j in zip(tr,tc):
			row=r+i
			col=c+j
			if canGo(row,col):
				grid[row][col]=3
				zeros-=1
				solve(row, col, zeros)
				grid[row][col]=0
				zeros+=1
		return

	l=len(grid)
	m=len(grid[0])
	nOnes,r,c=0,0,0
	for i in range(l):
		for j in range(m):
			if grid[i][j]==1:
				r=i;c=j
			elif grid[i][j]==-1:
				nOnes+=1
				
	zeros = l*m -2-nOnes
	solve(r, c, zeros)
	return  count

if __name__ == "__main__":
	grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
	grid = [[0,1],[2,0]]
	grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
	print(uniquePathsIII(grid,))


"""
similarQuestions::
		Sudoku Solver: Hard
		Unique Paths II: Medium
		Word Search II: Hard
"""
