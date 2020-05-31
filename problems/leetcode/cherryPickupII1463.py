"""
_________________________1463. Cherry Pickup II_________________________
Difficulty: Hard		Likes: 71		Dislikes: 3		Solution: None
Total Accepted: 2.2K		Total Submission: 3.6K		Acceptance Rate: 60.5%
Tags:  Dynamic Programming


Given a rows x cols matrix grid representing a field of cherries. Each cell
in grid represents the number of cherries that you can collect. You have
two robots that can collect cherries for you, Robot #1 is located at the
top-left corner (0,0) , and Robot #2 is located at the top-right corner
(0, cols-1) of the grid. Return the maximum number of cherries collection
using both robots  by following the rules below:  From a cell (i,j), robots
can move to cell (i+1, j-1) , (i+1, j) or (i+1, j+1). When any robot is
passing through a cell, It picks it up all cherries, and the cell becomes
an empty cell (0). When both robots stay on the same cell, only one of
them takes the cherries. Both robots cannot move outside of the grid
at any moment. Both robots should reach the bottom row in the grid.    


Example 1:Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.

Example 2:Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
Output: 28
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.

Example 3:Input: grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
Output: 22

Example 4:Input: grid = [[1,1],[1,1]]
Output: 4
 rows == grid.lengthcols == grid[i].length2 <= rows, cols <= 700 <= grid[i][j] <= 100 
"""

from functools import lru_cache
def cherryPickup(grid):
	@lru_cache(None)
	def foo(row, pc1, pc2):
		if row==len(grid):
			return 0
		cherry = grid[row][pc1] if pc1==pc2 else grid[row][pc1]+grid[row][pc2]
		return cherry+max(
			foo(row+1,c1,c2) for c1 in range(max(0,pc1-1),min(len(grid[0]), pc1+2)) for c2 in range(max(0,pc2-1),min(len(grid[0]), pc2+2))
		)
	return foo(0,0,len(grid[0])-1)





if __name__ == "__main__":
	grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
	print(cherryPickup(grid,))


"""
"""
