"""
_________________________675. Cut Off Trees for Golf Event_________________________
Difficulty: Hard		Likes: 563		Dislikes: 331		Solution: Available
Total Accepted: 35.9K		Total Submission: 103.4K		Acceptance Rate: 34.7%
Tags:  Breadth-first Search


You   are   asked   to   cut   off   trees   in  a  forest  for  a  golf  event.
The forest is represented as a non-negative 2D map, in this map:                
																																								
0 represents the obstacle can't be reached.                                     
1 represents the ground can be walked through.                                  
The   place  with  number  bigger  than  1  represents  a  tree  can  be  walked
through, and this positive number represents the tree's height.                 
																																								
In   one   step   you   can   walk   in   any   of   the  four  directions  top,
bottom,    left    and    right also    when   standing   in   a   point   which
is a tree you can decide whether or not to cut off the tree.                    
You  are  asked  to  cut  off  all  the  trees  in  this  forest in the order of
tree's  height  -  always  cut  off the tree with lowest height first. And after
cutting, the original place has the tree will become a grass (value 1).         
You   will   start   from   the   point   (0,  0)  and  you  should  output  the
minimum   steps   you   need   to   walk   to   cut   off   all  the  trees.  If
you can't cut off all the trees, output -1 in that situation.                   
You    are    guaranteed    that   no   two   trees   have   the   same   height
and there is at least one tree needs to be cut off.                             
																																								


Example 1:  Input: 
 [  [1,2,3],  [0,0,4],  [7,6,5] ] Output: 6
	  
Example 2:  Input: 
 [  [1,2,3],  [0,0,0],  [7,6,5] ] Output: -1
	  
Example 3:  Input: 
 [  [2,3,4],  [0,0,5],  [8,7,6] ] Output: 6
	   1 <= forest.length <= 50 1 <= forest[i].length <= 50 0 <= forest[i][j] <= 10^9  
"""


import functools, itertools, operator, bisect, array, collections, math
from typing import * 

class Solution:
		def cutOffTree(self, M: List[List[int]]) -> int:
				R = len(M)
				C = len(M[0])
				
				def dist(i,j):
						seen={(i,j)}
						s = collections.deque([(i,j,0)])
						mx = math.inf
						idx = None
						dist = math.inf
						
						while s:
							i,j,d = s.popleft()
							
							if 1 < M[i][j] < mx:
									mx = M[i][j]
									idx = (i, j)
									dist = d
									
							for x, y in ((i+1,j),(i,j+1),(i,j-1),(i-1,j)):
									if 0<=x<R and 0<=y<C and M[x][y] and (x,y) not in seen:
											seen.add((x,y))
											s.append((x,y,d+1))
							
						return dist, idx
				
				at = (0,0)
				t = 0
				while 1:
						d, idx = dist(*at)
						if idx==None:
								break

						at=idx
						t+=d
						M[at[0]][at[1]] = 1
						# print(at, d, t)
						
				return -1 if any(i>1 for row in M for i in row) else (-1 if t==math.inf else t)
				


if __name__ == "__main__":
	s = Solution()
	a = [  [1,2,3],  [0,0,0],  [7,6,5] ]
	print(s.cutOffTree(a))



"""
"""
