"""
_________________________85. Maximal Rectangle_________________________
Difficulty: Hard		Likes: 3362		Dislikes: 75		Solution: Available
Total Accepted: 197.6K		Total Submission: 513.3K		Acceptance Rate: 38.5%
Tags:  Array, Stack, Dynamic Programming, Hash Table


Given   a   rows   x   cols binary   matrix   filled  with  0's  and  1's,  find
the largest rectangle containing only 1's and return its area.                  
                                                                                
																				


Example 1:   Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
 Output: 6
  
Example 2:  Input: matrix = []
 Output: 0
  
Example 3:  Input: matrix = [["0"]]
 Output: 0
  
Example 4:  Input: matrix = [["1"]]
 Output: 1
  
Example 5:  Input: matrix = [["0","0"]]
 Output: 0
     rows == matrix.length cols == matrix.length 0 <= row, cols <= 200 matrix[i][j] is '0' or '1'.  
"""


import functools, itertools, operator, bisect, array, collections 
from typing import * 

class Solution:
	def largestRectangleArea(self, height):
		height.append(0)
		stack = [-1]
		ans = 0
		for i in range(len(height)):
			while height[i] < height[stack[-1]]:
				h = height[stack.pop()]
				w = i - stack[-1] - 1
				ans = max(ans, h * w)
			stack.append(i)
		height.pop()
		return ans

	def maximalRectangle(self, matrix: List[List[str]]) -> int:
		if not matrix:
			return 0
		
		R = len(matrix)
		C = len(matrix[0])
		row = [0]*C
		res = 0

		for r in matrix:
			for i,el in enumerate(r):
				if el=='1':
					row[i]+=1
				else:
					row[i] = 0
		
			res = max(res, self.largestRectangleArea(row))
			# print(row, res)
		return res	


if __name__ == "__main__":
	matrix = [
		["1","0","1","0","0"],
		["1","0","1","1","1"],
		["1","1","1","1","1"],
		["1","0","0","1","0"]
		]
	s = Solution()
	print(s.maximalRectangle(matrix))


"""
similarQuestions::
		Largest Rectangle in Histogram: Hard
		Maximal Square: Medium
"""
