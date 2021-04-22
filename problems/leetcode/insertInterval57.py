"""
_________________________57. Insert Interval_________________________
Difficulty: Hard		Likes: 1516		Dislikes: 178		Solution: Available
Total Accepted: 242.9K		Total Submission: 732.8K		Acceptance Rate: 33.2%
Tags:  Sort, Array


Given a set of non-overlapping intervals, insert a new interval
into the intervals (merge if necessary). You may assume that the
intervals were initially sorted according to their start times. 


Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

"""


import functools, itertools, operator, bisect, array 
from typing import *

class Solution:
	def insert(self, A: List[List[int]], a: List[int]) -> List[List[int]]:
		x, y = a
		if not A:		return [a]
		if y<A[0][0]:	return [a]+A
		if x>A[-1][-1]:	return A+[a]
		
		# def bisect_left(x, k):
		# 	l = 0
		# 	r = len(A)
		# 	while l<r:
		# 		m = (l+r)//2
		# 		if A[m][k] < x:	l = m + 1
		# 		else:			r = m
		# 	return l
		
		# def bisect_right(x, k):
		# 	l = 0
		# 	r = len(A)
		# 	while l<r:
		# 		m = (l+r)//2
		# 		if A[m][k] > x:	r = m
		# 		else:			l = m + 1
		# 	return l
		
		l = bisect.bisect_left([j for i,j in A], x)
		if y < A[l][0]:		
			return A[:l] + [a] + A[l:]
		r = bisect.bisect_right([j for i,j in A], y)
		return A[:l] + [[min(x, A[l][0]), max(y, A[r-1][1])]] + A[r:]

	def insert(self, A: List[List[int]], a: List[int]) -> List[List[int]]:
		x,y = a
		l = []
		r = []
		for i in A:
			if i[1] < x:
				l.append(i)
			elif i[0] > y:
				r.append(i)
			else:
				x = min(x, i[0])
				y = max(y, i[1])
		return l + [[x,y]] + r

	
		
		
			

if __name__ == "__main__":
	s=Solution()
	intervals = [[1,3],[6,9]]
	newInterval = [2,5]
 
	intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
	newInterval = [5.5,9]
	print(s.insert(intervals, newInterval))
	


"""
similarQuestions::
		Merge Intervals: Medium
		Range Module: Hard
"""
