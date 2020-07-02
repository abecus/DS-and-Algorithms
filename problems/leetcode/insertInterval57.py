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

class Solution:
	def insert(self, intervals, newInterval):
		if not intervals: return [newInterval]
		if intervals[0][0]>newInterval[1]:   return [newInterval]+intervals
		if intervals[-1][1]<newInterval[0]:   return intervals+[newInterval]
		
		start_list = [x[0] for x in intervals]
		end_list = [x[1] for x in intervals]
  
		i = bisect.bisect_left(end_list, newInterval[0])

		if newInterval[1] < intervals[i][0]:
			return intervals[:i] + [newInterval] + intervals[i:]
  
		start = min(newInterval[0], intervals[i][0])
		end = max(newInterval[1], intervals[i][1])

		j = i + bisect.bisect_right(start_list[i:],end)
  
		end = max(end, intervals[j-1][1])

		return intervals[:i] + [[start,end]] + intervals[j:]		


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
