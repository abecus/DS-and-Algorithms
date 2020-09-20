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


def uniquePathsIII(M) -> int:
    R = len(M)
    C = len(M[0])

    def foo(i, j, z):
        t = 0
        for dx, dy in zip((1, 0, -1, 0), (0, 1, 0, -1)):
            x = i+dx
            y = j+dy
            if 0 <= x < R and 0 <= y < C:
                if M[x][y] == 0:
                    M[x][y] = 3
                    t += foo(x, y, z-1)
                    M[x][y] = 0
                elif z == 0 and M[x][y] == 2:
                    t += 1
        return t

    sx = 0
    sy = 0
    cz = 0
    for i in range(R):
        for j in range(C):
            if M[i][j] == 1:
                sx = i
                sy = j
            elif M[i][j] == 0:
                cz += 1

    return foo(sx, sy, cz)


if __name__ == "__main__":
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
    # grid = [[0,1],[2,0]]
    # grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    print(uniquePathsIII(grid,))


"""
similarQuestions::
		Sudoku Solver: Hard
		Unique Paths II: Medium
		Word Search II: Hard
"""
