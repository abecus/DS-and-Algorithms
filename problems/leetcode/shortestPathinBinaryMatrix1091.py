"""
_________________________1091. Shortest Path in Binary Matrix_________________________
Difficulty: Medium		Likes: 424		Dislikes: 42		Solution: None
Total Accepted: 32.1K		Total Submission: 84.3K		Acceptance Rate: 38.1%
Tags:  Breadth-first Search


In an N by N square grid, each cell is either empty (0) or blocked (1).
A clear path from top-left to bottom-right has length k if and only if
it is composed of cells C_1, C_2, ..., C_k such that:  Adjacent cells
C_i and C_{i+1} are connected 8-directionally (ie., they are different
and share an edge or corner) C_1 is at location (0, 0) (ie. has value
grid[0][0]) C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c]
== 0).  Return the length of the shortest such clear path from top-left
to bottom-right.  If such a path does not exist, return -1.   


Example 1:Input: [[0,1],[1,0]]
Output: 2

Example 2:Input: [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
 Note:
1 <= grid.length == grid[0].length <= 100grid[r][c] is 0 or 1
"""


import functools
import itertools
import operator
import bisect
import array
import math
from typing import *


class Solution:
	def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
		r = len(grid)
		c = len(grid[0])

		if grid[-1][-1] == 1 or grid[0][0] == 1:
			return -1

		dx = [1,1,1,0,0,-1,-1,-1]
		dy = [0,1,-1,1,-1,0,1,-1]

		s = collections.deque([(r-1, c-1, 1)])

		while s:
			x, y, d = s.popleft()

			if x==y==0:
				return d

			for _x, _y in zip(dx, dy):
				nx = x + _x
				ny = y + _y

				if 0 <= nx < r and 0 <= ny < c and grid[nx][ny]==0:
					grid[nx][ny] = -1
					s.append((nx, ny, d+1))

		return -1


if __name__ == "__main__":
	# arr = [[0, 1], [1, 0]]
	# arr = [ [0,1,0],
	# 		[1,1,0],
	# 		[1,1,0]]
	arr = [
		[0,0,1,0,0,0,0],
		[0,1,0,0,0,0,1],
		[0,0,1,0,1,0,0],
		[0,0,0,1,1,1,0],
		[1,0,0,1,1,0,0],
		[1,1,1,1,1,0,1],
		[0,0,1,0,0,0,0]
		]

	s = Solution()
	print(s.shortestPathBinaryMatrix(arr))


"""
"""
