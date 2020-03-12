"""
_________________________746. Min Cost Climbing Stairs_________________________
Difficulty: Easy		Likes: 1564		Dislikes: 354		Solution: Available
Total Accepted: 124.5K		Total Submission: 254K		Acceptance Rate: 49.0%
Tags:  Dynamic Programming, Array



 On a staircase, the i-th step has some non-negative cost cost[i] assigned
(0 indexed).
 
 Once you pay the cost, you can either climb one or two
steps. You need to find minimum cost to reach the top of the floor, and you
can either start from the step with index 0, or the step with index 1.
  


Example 1:
Input: cost = [10, 15, 20]
Output: 15

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Note:
cost will have a length in the range [2, 1000].Every cost[i] will be an integer in the range [0, 999].

"""

from functools import lru_cache
def minCostClimbingStairs(cost):
	# cost.append(0)
	# @lru_cache(None)
	# def helper(i):
	# 	if i<2:
	# 		if i<0:
	# 			return 0
	# 		return cost[i]
	# 	return cost[i]+min(helper(i-1), helper(i-2))
	# return helper(len(cost)-1)

	a=cost[0]
	b=cost[1]
	for i in range(2,len(cost)):
		b,a=cost[i]+min(a,b),b
	return min(a,b)
 
 
if __name__ == "__main__":
	cost = [0,0,0,0]
	# cost = [10, 15, 20]
	# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
	print(minCostClimbingStairs(cost,))


"""
similarQuestions::
		Climbing Stairs: Easy
"""
