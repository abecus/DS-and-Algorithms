"""
542. 01 Matrix
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:
Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""

from collections import deque
from typing import *
import math


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        q = deque()

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    q.append((i, j))
                else:
                    matrix[i][j] = math.inf

        while q:
            x, y = q.popleft()
            for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] > matrix[x][y]+1:
                    matrix[nx][ny] = matrix[x][y]+1
                    q.append((nx, ny))

        return matrix


if __name__ == "__main__":
    mat = [[0, 0, 0],
           [0, 1, 0],
           [1, 1, 1]]

    mat = [[0, 1, 1],
           [1, 1, 1],
           [1, 1, 1]]

    # mat = [[1,1,1],
    #        [1,1,1],
    #        [1,1,0]]

    ans = updateMatrix(mat)
    print(*ans, sep='\n')
