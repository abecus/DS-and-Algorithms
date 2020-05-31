"""
_________________________994. Rotting Oranges_________________________
Difficulty: Medium		Likes: 1259		Dislikes: 170		Solution: Available
Total Accepted: 77.3K		Total Submission: 164.3K		Acceptance Rate: 47.0%
Tags:  Breadth-first Search


In a given grid, each cell can have one of three values:  the value 0
representing an empty cell; the value 1 representing a fresh orange;
the value 2 representing a rotten orange.  Every minute, any fresh
orange that is adjacent (4-directionally) to a rotten orange becomes
rotten. Return the minimum number of minutes that must elapse until no
cell has a fresh orange.  If this is impossible, return -1 instead.    


Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1

Example 3:
Input: [[0,2]]
Output: 0
 Note:
1 <= grid.length <= 101 <= grid[0].length <= 10grid[i][j] is only 0, 1, or 2.
"""


def orangesRotting(grid):
        r=len(grid)
        c=len(grid[0])
        
        def get_adj(i,j):
            for x,y in zip([1,-1,0,0],[0,0,-1,1]):
                if 0<=i+x<r and 0<=j+y<c:
                    yield (i+x,j+y)
                    
        q=[(i,j) for i in range(r) for j in range(c) if grid[i][j]==2]
        
        res=0
        temp=[]
        while q:
            i,j=q.pop()
            for x,y in get_adj(i,j):
                if grid[x][y]==1:
                    grid[x][y]=2
                    temp.append((x,y))
            if not q:
                res+=1
                q=temp.copy()
                temp=[]
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    return -1
        
        return res-1 if res else res
                    

if __name__ == "__main__":
	grid = [[2,1,1],[1,1,0],[0,1,1]]
	grid = [[2,1,1],[0,1,1],[1,0,1]]
	grid = [[0,1]]
 
	print(orangesRotting(grid,))


"""
similarQuestions::
		Walls and Gates: Medium
"""
