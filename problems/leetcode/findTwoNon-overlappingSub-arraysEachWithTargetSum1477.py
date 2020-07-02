"""
_________________________1477. Find Two Non-overlapping Sub-arrays Each With Target Sum_________________________
Difficulty: Medium		Likes: 197		Dislikes: 12		Solution: None
Total Accepted: 4.4K		Total Submission: 18.2K		Acceptance Rate: 24.1%
Tags:  Dynamic Programming


Given an array of integers arr and an integer target. You have to find two
non-overlapping sub-arrays of arr each with sum equal target. There can be
multiple answers so you have to find an answer where the sum of the lengths of
the two sub-arrays is minimum. Return the minimum sum of the lengths of the two
required sub-arrays, or return -1 if you cannot find such two sub-arrays.   


Example 1:
Input: arr = [3,2,2,4,3], target = 3
Output: 2

Example 2:
Input: arr = [7,3,4,7], target = 7
Output: 2

Example 3:
Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1

Example 4:
Input: arr = [5,5,4,4,5], target = 3
Output: -1

Example 5:
Input: arr = [3,1,1,1,5,1,2,1], target = 3
Output: 3
 1 <= arr.length <= 10^51 <= arr[i] <= 10001 <= target <= 10^8
"""


import functools, itertools, operator, bisect, array, math
from typing import *


class Solution:
	def minSumOfLengths(self, arr: List[int], target: int) -> int:
		prefix = {0: -1}
		best_till = [math.inf] * len(arr)
		ans = best = math.inf
		for i, curr in enumerate(itertools.accumulate(arr)):
			if curr - target in prefix:
				end = prefix[curr - target]
				if end > -1:
					ans = min(ans, i - end + best_till[end])
				best = min(best, i - end)
			best_till[i] = best
			prefix[curr] = i
		print(best_till, prefix)
		# return -1 if ans == math.inf else ans

		ps = {0 : -1}
		bestPrefix = []
		ans = best = math.inf
		
		for i, v in  enumerate(itertools.accumulate(arr)):
			if v - target in ps:
				end = ps[v - target]

				if end > -1:
					ans = min( ans, i - end + best[end] )                
				best = min( best, i - end )
				
			bestPrefix.append( best )
			ps[curr] = i

		print(bestPrefix, ps)
		return ans
		


if __name__ == "__main__":
	arr = [3,1,1,1,5,1,2,1]
	target = 3
	s= Solution()
	print(s.minSumOfLengths(arr, target))


"""
"""
