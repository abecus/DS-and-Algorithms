"""
_________________________934. Shortest Bridge_________________________
Difficulty: Medium		Likes: 656		Dislikes: 50		Solution: Available
Total Accepted: 23.7K		Total Submission: 50.4K		Acceptance Rate: 47.0%
Tags:  Breadth-first Search, Depth-first Search


In a given 2D binary array A, there are two islands.  (An island is
a 4-directionally connected group of 1s not connected to any other
1s.) Now, we may change 0s to 1s so as to connect the two islands
together to form 1 island. Return the smallest number of 0s that must
be flipped.  (It is guaranteed that the answer is at least 1.)   


Example 1:Input: A = [[0,1],[1,0]]
Output: 1

Example 2:Input: A = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 2 <= A.length == A[0].length <= 100A[i][j] == 0 or A[i][j] == 1

"""


import functools, itertools, operator, bisect, array, sortedcontainers 

class Solution:
    def shortestBridge(self, A) -> int:
        R, C = len(A), len(A[0])
        dirs = [(0,0),(-1,0),(0,-1),(1,0),(0,1)]
        
        def floodfill(i,j):
            yield i,j
            A[i][j]=-1

            for x,y in dirs:
                if 0<=x+i<R and 0<=y+j<C and A[x+i][y+j]==1:
                    yield from floodfill(x+i, y+j)
                
        a=collections.deque()
        def foo():
            for i in range(R):
                for j in range(C):
                    if A[i][j]==1:
                        for v in floodfill(i,j):
                            a.append(v) 
                        return

        foo()
        step = 0
        while a:
            for _ in range(len(a)):
                x,y=a.popleft()
                for dx,dy in dirs:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<R and 0<=ny<C and A[nx][ny]!=2:
                        if A[nx][ny] == 0:
                            A[nx][ny]=2
                            a.append([nx,ny])
                        elif A[nx][ny] == 1:
                            return step
            step+=1
        return step
          
        # dist = lambda p1,p2: abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        # return min(dist(p1, p2) for p1 in a for p2 in b)-1

if __name__ == "__main__":
	pass


"""
"""
