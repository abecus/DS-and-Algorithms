"""
_________________________84. Largest Rectangle in Histogram_________________________
Difficulty: Hard		Likes: 4431		Dislikes: 93		Solution: Available
Total Accepted: 295.4K		Total Submission: 824K		Acceptance Rate: 35.8%
Tags:  Array, Stack


Given  n non-negative integers representing the histogram's bar height where the
width of each bar is 1, find the area of largest rectangle in the histogram.    
                                                                                
                                                                                
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
                                                                                
                                                                                
The largest rectangle is shown in the shaded area, which has area = 10 unit.    
                                                                                
                                                                                


Example: 
 Input: [2,1,5,6,2,3]
 Output: 10
  
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

if __name__ == "__main__":
	arr = [2,1,2,0,2,1,1,1,2]
	s = Solution()
	print(s.largestRectangleArea(arr))


"""
similarQuestions::
		Maximal Rectangle: Hard
"""
