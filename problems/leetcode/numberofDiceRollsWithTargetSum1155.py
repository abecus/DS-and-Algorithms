"""
_________________________1155. Number of Dice Rolls With Target Sum_________________________
Difficulty: Medium		Likes: 640		Dislikes: 36		Solution: None
Total Accepted: 36.8K		Total Submission: 74.8K		Acceptance Rate: 49.3%
Tags:  Dynamic Programming


You have d dice, and each die has f faces numbered 1, 2, ..., f. Return
the number of possible ways (out of fd total ways) modulo 10^9 + 7
to roll the dice so the sum of the face up numbers equals target.   


Example 1:
Input: d = 1, f = 6, target = 3
Output: 1
You throw one die with 6 faces.  There is only one way to get a sum of 3.

Example 2:
Input: d = 2, f = 6, target = 7
Output: 6
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:
Input: d = 2, f = 5, target = 10
Output: 1

Example 4:
Input: d = 1, f = 2, target = 3
Output: 0
You throw one die with 2 faces.  There is no way to get a sum of 3.

Example 5:
Input: d = 30, f = 30, target = 500
Output: 222616187
The answer must be returned modulo 10^9 + 7.
 1 <= d, f <= 301 <= target <= 1000
"""


import functools, itertools, operator, bisect, array 

class Solution:
	def numRollsToTarget(self, d: int, f: int, target: int) -> int:
		if d*f == target:				return 1
		self.M = 10**9 + 7
		
		# @functools.lru_cache(None)
		# def foo(d, target):
		# 	if d*f < target or target < d:	return 0
		# 	if d == 1 and target <= f:	return 1
				
		# 	temp = 0
		# 	for i in reversed(range(1, f+1)):
		# 		temp = (temp + foo(d - 1, target - i)) % self.M
		# 	return	temp
   
		# return foo(d, target)

		@functools.lru_cache(None)
		def foo(d, s):
			if s + d*f < target or s > target:	return 0
			if d == 1 and 0 < target - s <= f:	return 1
				
			temp = 0
			for i in reversed(range(1, f+1)):
				temp = (temp + foo(d - 1, s + i)) % self.M
			return	temp
   
		return foo(d, 0)


if __name__ == "__main__":
	d = 30
	f = 30
	target = 500
#  6
	
	s = Solution()
	print(s.numRollsToTarget(d, f, target))


"""
"""
