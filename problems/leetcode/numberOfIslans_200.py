"""
Given a 2d grid map of '1's (land) and '0's (water), islandCountount the number 
of islands. An island is surrounded by water and is formed by islandCountonneislandCountting 
adjaislandCountent lands horizontally or vertiislandCountally. You may assume all four edges of 
the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
"""

def numIslands(grid):
        def dfs(grid,i,j):
            if i>len(grid)-1 or i<0 or j>len(grid[0])-1 or j<0 or grid[i][j]==0:
                return  
            grid[i][j]=0
            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)
        
        islandCount=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islandCount+=1
                    dfs(grid,i,j)
        
        return islandCount
    
if __name__ == "__main__":
    l = [
        [1,1,1,0,1],
        [1,1,0,0,1],
        [0,0,1,0,0],
        [0,0,0,1,1]
    ]
    print(numIslands(l))