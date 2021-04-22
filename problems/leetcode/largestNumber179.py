"""
_________________________179. Largest Number_________________________
Difficulty: Medium		Likes: 2227		Dislikes: 257		Solution: Available
Total Accepted: 199K		Total Submission: 680.6K		Acceptance Rate: 29.2%
Tags:  Sort


Given      a      list      of      non      negative      integers,     arrange
them such that they form the largest number.                                    
																																								


Example 1: 
 Input: [10,2]
 Output: "210"
 
Example 2: 
 Input: [3,30,34,5,9]
 Output: "9534330"
	Note: The result may be very large, so you need to return a string instead of an integer.
 
"""
import functools
import itertools
import operator
import bisect
import array
import collections
from typing import *
from functools import cmp_to_key


class Solution:
	def largestNumber(self, nums: List[int]) -> str:
		def cmp_fun(a, b):
			return -1 if a+b > b+a else (1 if a+b < b+a else 0)
		s = "".join(map(str, sorted(map(str, nums), key=cmp_to_key(cmp_fun))))
		return "0" if s[0]=='0' else s

if __name__ == "__main__":
	s = Solution()
	print(s.largestNumber([3, 30, 34, 5, 9]))


"""
"""
