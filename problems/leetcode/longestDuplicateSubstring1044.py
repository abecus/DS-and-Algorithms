"""
_________________________1044. Longest Duplicate Substring_________________________
Difficulty: Hard		Likes: 625		Dislikes: 226		Solution: Available
Total Accepted: 29.2K		Total Submission: 91.6K		Acceptance Rate: 31.9%
Tags:  Hash Table, Binary Search


Given a string S, consider all duplicated substrings: (contiguous)
substrings of S that occur 2 or more times.  (The occurrences may
overlap.) Return any duplicated substring that has the longest possible
length.  (If S does not have a duplicated substring, the answer is "".)   


Example 1:
Input: "banana"
Output: "ana"

Example 2:
Input: "abcd"
Output: ""
 Note:
2 <= S.length <= 10^5S consists of lowercase English letters.

"""


import functools
import itertools
import operator
import bisect
import array
import collections
from typing import *


class Solution:
	def longestDupSubstring(self, S: str) -> str:
		def getMaxLength(m):
			# calculate hash value
			s = 0
			for i in range(m):
				s = (26 * s + mapper[i]) % mod

			power = pow(26, m, mod)
			seen = {s}
			# find hash values
			for i in range(m, len(S)):
				s = (s*26 - (mapper[i-m] * power) + mapper[i]) % mod
				if s in seen:
					return i-m+1
				seen.add(s)
			return ''

		mod = (1 << 63)-1
		mapper = [ord(x)-97 for x in S]
		l = 0
		r = len(S)
		res = 0
		while l < r:
			m = (l+r+1)//2
			s = getMaxLength(m)
			if s:
				l = m
				res = s
			else:
				r = m-1
		return S[res: res+l]


if __name__ == "__main__":
	s = Solution()
	st = "banana"
	res = s.longestDupSubstring(st)
"""
"""
