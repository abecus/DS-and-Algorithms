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

def updateMatrix(mat):
    row = len(mat)
    col = len(mat[0])
    q = deque()
    
    for i in range(row):
        for j in range(col):
            val = mat[i][j]
            if not val:
                q.append((i ,j, val))
                
    
    visited = set()
    while q:
        x, y, d = q.popleft()            
        for dx, dy in zip([1,0,-1,0], [0,1,0,-1]):
            nx = x+dx
            ny = y+dy
            if (nx,ny) not in visited and\
                0<=nx<row and 0<=ny<col and mat[nx][ny]:
                    mat[nx][ny] = d+1
                    q.append((nx,ny,d+1))
                    visited.add((nx,ny))
                                   
    return mat

        
if __name__ == "__main__":
    mat = [[0,0,0], [0,1,0], [1,1,1]]
    mat = [[0,1,1], 
           [1,1,1], 
           [1,1,1]]
    # mat = [[1,1,1], 
    #        [1,1,1], 
    #        [1,1,0]]
    ans = updateMatrix(mat)
    for i in ans:
        print(i)