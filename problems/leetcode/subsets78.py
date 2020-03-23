"""
_________________________78. Subsets_________________________
Difficulty: Medium		Likes: 3013		Dislikes: 72		Solution: Available
Total Accepted: 497.3K		Total Submission: 852.5K		Acceptance Rate: 58.3%
Tags:  Bit Manipulation, Array, Backtracking


Given a set of distinct integers, nums, return all possible subsets (the
power set). Note: The solution set must not contain duplicate subsets. 


Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

import itertools
def subsets(nums):
	
	def powerset(i,com,l):
		res.append(com.copy())
		for idx in range(i,l):
			com.append(nums[idx])
			powerset(idx+1,com,l)
			com.pop()
	res=[]
	powerset(0,[],len(nums))
	return res



if __name__ == "__main__":
	nums = [1,2,3]
	print(subsets(nums,))


"""
similarQuestions::
		Subsets II: Medium
		Generalized Abbreviation: Medium
		Letter Case Permutation: Easy
"""
