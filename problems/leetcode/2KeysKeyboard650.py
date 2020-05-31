"""
_________________________650. 2 Keys Keyboard_________________________
Difficulty: Medium		Likes: 899		Dislikes: 69		Solution: Available
Total Accepted: 46K		Total Submission: 95.6K		Acceptance Rate: 48.1%
Tags:  Dynamic Programming


Initially on a notepad only one character 'A' is present. You can perform
two operations on this notepad for each step:  Copy All: You can copy all
the characters present on the notepad (partial copy is not allowed). Paste:
You can paste the characters which are copied last time.    Given a number
n. You have to get exactly n 'A' on the notepad by performing the minimum
number of steps permitted. Output the minimum number of steps to get n 'A'. 


Example 1:
Input: 3
Output: 3
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
 Note:
The n will be in the range [1, 1000].
 
"""


def minSteps(n):

	from functools import lru_cache
	@lru_cache(None)
	def f(x,copied):
		if x>n:
			return float('inf')
		if x==n:
			return 0
		return min(
			2+f(x+x, x),
			1+f(x+copied, copied)
		)

	# temp = 1+f(1, 1)
	# print(f.cache_info())
	return 1+f(1, 1)

# ________________________________________________________
	# dp=[0]+[float('inf')]*n
	# for i in range(n+1):
	# 	temp=float('inf')
	# 	for j in range(2, i//2 +1):
	# 		if i%j ==0:
	# 			temp=min(temp, dp[j]+(i//j))
	# 	dp[i]=min(temp, i)
	# return dp[-1]
 
# ________________________________________________________
	# ans=0
	# d=2
	# while n>1:
	# 	while not n%d:
	# 		n//=d
	# 		ans+=d
	# 	d+=1
	# return ans


if __name__ == "__main__":
	n = 3
	print(minSteps(n,))

	# def foo(x):
	# 	if x<2:
	# 		if x==1:
	# 			return 0
	# 		return float('inf')
	# 	return min(
	# 			foo((x>>1))+2,
	# 			foo((x-(x>>2)))+1
	# 			)

	# print(foo(n,0))
"""
similarQuestions::
		4 Keys Keyboard: Medium
		Broken Calculator: Medium
"""
