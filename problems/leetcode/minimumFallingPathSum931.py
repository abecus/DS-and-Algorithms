"""
_________________________931. Minimum Falling Path Sum_________________________
Difficulty: Medium		Likes: 337		Dislikes: 37		Solution: Available
Total Accepted: 24.7K		Total Submission: 41.6K		Acceptance Rate: 59.4%
Tags:  Dynamic Programming


Given a square array of integers A, we want the minimum sum of a falling path through A.
A falling path starts at any element in the first row, and chooses one element from each row.
The next row's choice must be in a column that is different from the previous row's column by at most one.
Example 1:


Input: [[1,2,3],[4,5,6],[7,8,9]]

Output: 12

Explanation:

The possible falling paths are:



[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]

The falling path with the smallest sum is [1,4,7], so the answer is 12.
Note:

1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100
"""

from functools import lru_cache
def minFallingPathSum(A):
	l = len(A)
	if l==1:
		return A[0][0]

	@lru_cache(None)
	def helper(i, j, l=l, A=A):
		if i<0 or i>=l or j<0 or j>=l:
			return float('inf')

		if i==0 and 0<=j<l:
			return A[i][j]

		return min(helper(i-1, j-1, ), helper(i-1, j, ), helper(i-1, j+1, ))+A[i][j]
	
	
	return min(helper(l-1, i) for i in range(l))


if __name__ == "__main__":
	A = [
     	[1,0,-5],
      	[-10,5,-100],
       	[7,8,1]
         ]
	print(minFallingPathSum(A,))
