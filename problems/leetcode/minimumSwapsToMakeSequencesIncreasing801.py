"""
_________________________801. Minimum Swaps To Make Sequences Increasing_________________________
Difficulty: Medium		Likes: 761		Dislikes: 55		Solution: Available
Total Accepted: 23.3K		Total Submission: 61.6K		Acceptance Rate: 37.8%
Tags:  Dynamic Programming


We have two integer sequences A and B of the same non-zero length.
We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences.
At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)
Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.

Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation: 
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.

Note:

A, B are arrays with the same length, and that length will be in the range [1, 1000].
A[i], B[i] are integer values in the range [0, 2000].

"""

def minSwap(A, B):
	n=len(A)
	swap = 1
	fix = 0
	
	for i in range(1, n):
		if A[i-1] >= B[i] or B[i-1] >= A[i]:
			swap += 1
		elif A[i-1] >= A[i] or B[i-1] >= B[i]:
			swap, fix = fix + 1, swap
		else:
			mn = min(swap, fix)
			swap = mn + 1
			fix = mn
		# print(i, swap, fix)
	return min(swap, fix)

if __name__ == "__main__":
	A = [1,3,5,4]
	B = [1,2,3,7]
	A = [0,4,4,5,9]
	B = [0,1,6,8,10]
	print(minSwap(A,B,))


"""
"""
