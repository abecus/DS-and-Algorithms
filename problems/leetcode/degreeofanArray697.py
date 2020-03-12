"""
_________________________697. Degree of an Array_________________________
Difficulty: Easy		Likes: 698		Dislikes: 638		Solution: Available
Total Accepted: 69.7K		Total Submission: 132.3K		Acceptance Rate: 52.7%
Tags:  Array


Given a non-empty array of non-negative integers nums, the degree
of this array is defined as the maximum frequency of any one of its
elements. Your task is to find the smallest possible length of a
(contiguous) subarray of nums, that has the same degree as nums. 


Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
The input array has a degree of 2 because both elements 1 and 2 appear twice.
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:
nums.length will be between 1 and 50,000.nums[i] will be an integer between 0 and 49,999.
"""

import collections
def findShortestSubArray(nums):
	d=collections.defaultdict(list)
	for i, el in enumerate(nums):
		d[el].append(i) 
	
	numsDegree = max(len(x[1]) for x in d.items())
	# print(numsDegree)
	
	m=len(nums)
	for _, v in d.items():
		if len(v)==numsDegree:
			m=min(m, v[-1]-v[0]+1)
	return m

	
	

if __name__ == "__main__":
	nums = [1,2,2,3,1,4,2]
	nums = [1, 2, 2, 3, 1]
	print(findShortestSubArray(nums,))


"""
similarQuestions::
		Maximum Subarray: Easy
"""
