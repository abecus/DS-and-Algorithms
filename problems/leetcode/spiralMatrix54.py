"""
_________________________54. Spiral Matrix_________________________
Difficulty: Medium		Likes: 2327		Dislikes: 565		Solution: Available
Total Accepted: 367K		Total Submission: 1.1M		Acceptance Rate: 33.8%
Tags:  Array


Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order. 


Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""


import functools, itertools, operator, bisect, array 
from typing import *


class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		if not matrix:	return
		
		c1, c2 = 0, len(matrix[0]) - 1
		r1, r2 = 0, len(matrix)-1

		def getLayer(c1,c2,r1,r2):
			for i in range(c1, c2+1):			yield r1, i
			for i in range(r1+1, r2+1):			yield i, c2
			if r1 < r2 and c1 < c2:
				for i in range(c2-1, c1, -1):	yield r2, i
				for i in range(r2, r1, -1):			yield i, c1

		res = []
		while r1 <= r2 and c1 <= c2:
			for x, y in getLayer(c1, c2, r1, r2):
				res.append(matrix[x][y])
			r1+=1
			r2-=1
			c1+=1
			c2-=1

		return res

			
if __name__ == "__main__":
	mat = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9,10,11,12],
	[13,14,15,16],
	[17,18,19,20]
	]
	# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

	print(Solution.spiralOrder(1, mat))


"""
similarQuestions::
		Spiral Matrix II: Medium
		Spiral Matrix III: Medium
"""
