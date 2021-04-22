"""
_________________________39. Combination Sum_________________________
Difficulty: Medium		Likes: 4386		Dislikes: 128		Solution: Available
Total Accepted: 581.3K		Total Submission: 1M		Acceptance Rate: 56.8%
Tags:  Backtracking, Array


Given   a   set   of   candidate   numbers   (candidates)  (without  duplicates)
and    a    target    number    (target),    find    all   unique   combinations
in candidates where the candidate numbers sums to target.                       
The        same        repeated        number        may        be        chosen
from candidates unlimited number of times.                                      
Note:                                                                           
																				
All numbers (including target) will be positive integers.                       
The solution set must not contain duplicate combinations.                       
																				
																				


Example 1: 
 Input: candidates = [2,3,6,7], target = 7,
 [
   [7],
   [2,2,3]
 ]
  
Example 2: 
 Input: candidates = [2,3,5], target = 8,
 [
   [2,2,2,2],
   [2,3,3],
   [3,5]
 ]
     1 <= candidates.length <= 30 1 <= candidates[i] <= 200 Each element of candidate is unique.
 1 <= target <= 500  
"""


import functools, itertools, operator, bisect, array, collections 
from typing import * 


class Solution:
	def combinationSum(self, A:[int], t: int) -> [[int]]:
		A.sort()
		while A and A[-1]>t:
			A.pop()
			
		res = []
		def foo(t, p):
			if t==0:
				return res.append(p.copy())
			
			for k in range(len(A)):
				if p and p[-1]>A[k]:	
					continue
				if A[k]>t:
					break
				foo(t-A[k], p+[A[k]])
				
		foo(t, [])
		return res

if __name__ == "__main__":
	A = [2,3,6,7]; t = 7
	# A = [1]; t = 2
	s = Solution()
	print(s.combinationSum(A, t))


"""
similarQuestions::
		Letter Combinations of a Phone Number: Medium
		Combination Sum II: Medium
		Combinations: Medium
		Combination Sum III: Medium
		Factor Combinations: Medium
		Combination Sum IV: Medium
"""
