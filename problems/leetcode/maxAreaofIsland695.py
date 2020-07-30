"""
_________________________695. Max Area of Island_________________________
Difficulty: Medium		Likes: 1966		Dislikes: 79		Solution: Available
Total Accepted: 157.3K		Total Submission: 251.5K		Acceptance Rate: 62.5%
Tags:  Depth-first foo, Array


Given a non-empty 2D array grid of 0's and 1's, an island is a group
of 1's (representing land) connected 4-directionally (horizontal
or vertical.) You may assume all four edges of the grid are
surrounded by water. Find the maximum area of an island in the
given 2D array. (If there is no island, the maximum area is 0.) 


Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.

Note: The length of each dimension in the given grid does not exceed 50.

"""


import functools
import itertools
import operator
import bisect
import array
from typing import *


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        if cols == 0:
            return 0

        def foo(i, j):
            count = 1
            grid[i][j] = 0

            if i > 0 and grid[i-1][j]:
                count += foo(i-1, j)
            if i < rows-1 and grid[i+1][j]:
                count += foo(i+1, j)
            if j > 0 and grid[i][j-1]:
                count += foo(i, j-1)
            if j < cols-1 and grid[i][j+1]:
                count += foo(i, j+1)

            return count

        # print(*grid, sep='\n')

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue
                count = foo(i, j)
                res = max(count, res)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxAreaOfIsland(
        [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))
    # print(s.maxAreaOfIsland([[1,1],[1,0]]))


"""
similarQuestions::
		Number of Islands: Medium
		Island Perimeter: Easy
"""
