"""
_________________________400. Nth Digit_________________________
Difficulty: Medium		Likes: 375		Dislikes: 1067		Solution: None
Total Accepted: 59.5K		Total Submission: 187.2K		Acceptance Rate: 31.8%
Tags:  Math


Find       the       nth       digit      of      the      infinite      integer
sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...                                 
Note:                                                                           
n      is      positive      and      will      fit     within     the     range
of a 32-bit signed integer (n < 231).
										  
																				
																				


Example 1: 
 Input:
 3
 
 Output:
 3
   
Example 2: 
 Input:
 11
 
 Output:
 0
 
 The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
  
"""


import functools, itertools, operator, bisect, array, collections 
from typing import * 

class Solution:
	def findNthDigit(self, n: int) -> int:
		if n < 9:
			return n
		
		i = 0
		s = 0
		while s < n:
			s += 9 * pow(10, i) * (i+1)
			i+=1

		l = 10**(i-1) - 1
		n -= l
		d, r = divmod(n, i)

		l += d-1
		return int(str(l)[r])


if __name__ == "__main__":
	s =  Solution()
	print(s.findNthDigit(100))


"""
"""
