"""
_________________________312. Burst Balloons_________________________
Difficulty: Hard		Likes: 1972		Dislikes: 56		Solution: Available
Total Accepted: 85.9K		Total Submission: 171.1K		Acceptance Rate: 50.2%
Tags:  Divide and Conquer, Dynamic Programming


Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number
on it represented by array nums. You are asked to burst all the balloons. If
the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i. After the burst, the left and
right then becomes adjacent. Find the maximum coins you can collect by bursting
the balloons wisely. Note:  You may imagine nums[-1] = nums[n] = 1. They are
not real therefore you can not burst them. 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100  


Example:
Input: [3,1,5,8]
Output: 167 
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""


def maxCoins(nums):
	nums=[1]+nums+[1]
	n=len(nums)
	dp=[[0]*n for _ in range(n)]
	
	for l in range(2, n):
		for i in range(n-l):
			j = i+l
			lr_prod = nums[i]*nums[j]
			dp[i][j] = max(dp[i][j], max(dp[i][k]+nums[k]*lr_prod+dp[k][j] for k in range(i+1,j)))
	return dp[0][n-1]





if __name__ == "__main__":
	nums = []
	print(maxCoins(nums,))


"""
similarQuestions::
		Minimum Cost to Merge Stones: Hard
"""
