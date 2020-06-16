"""
_________________________174. Dungeon Game_________________________
Difficulty: Hard		Likes: 1240		Dislikes: 33		Solution: Available
Total Accepted: 85.6K		Total Submission: 287.8K		Acceptance Rate: 29.7%
Tags:  Binary Search, Dynamic Programming


table.dungeon, .dungeon th, .dungeon td {
	 border:3px solid black;
 }
 
 
.dungeon th, .dungeon td {
		 text-align: center;
		 height: 70px;
		
width: 70px;
 }
	The demons had captured the princess (P) and imprisoned her
in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms
laid out in a 2D grid. Our valiant knight (K) was initially positioned in the
top-left room and must fight his way through the dungeon to rescue the princess.
The knight has an initial health point represented by a positive integer.
If at any point his health point drops to 0 or below, he dies immediately.
Some of the rooms are guarded by demons, so the knight loses health (negative
integers) upon entering these rooms; other rooms are either empty (0's) or
contain magic orbs that increase the knight's health (positive integers). In
order to reach the princess as quickly as possible, the knight decides to move
only rightward or downward in each step.   Write a function to determine the
knight's minimum initial health so that he is able to rescue the princess.
For example, given the dungeon below, the initial health of the knight must
be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.  
 -2 (K) -3 3   -5 -10 1   10 30 -5 (P)      Note:  The knight's health has no
upper bound. Any room can contain threats or power-ups, even the first room
the knight enters and the bottom-right room where the princess is imprisoned. 


"""


import functools, itertools, operator, bisect, array 
from typing import *

class Solution:
		def calculateMinimumHP(self, dungeon):
				@functools.lru_cache(None)
				def foo(i,j):
						if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:     
								return dungeon[i][j]

						temp = float('inf')

						if i < len(dungeon) - 1:
								left = foo(i + 1, j)
								temp = min(temp, left)

						if j < len(dungeon[0]) - 1:
								right = foo(i, j + 1)
								temp = min(temp, right)
								
						return 1 if temp <= dungeon[i][j] else temp - dungeon[i][j]
				
				dungeon[-1][-1] = 1 if dungeon[-1][-1] >= 0 else -dungeon[-1][-1] + 1

				return foo(0, 0)
				


if __name__ == "__main__":
	s = Solution()
	print(s.calculateMinimumHP([[-2,-3],
															[-5,-10]]
														 )
				)


"""
similarQuestions::
		Unique Paths: Medium
		Minimum Path Sum: Medium
		Cherry Pickup: Hard
"""
