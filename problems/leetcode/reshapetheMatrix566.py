"""
_________________________566. Reshape the Matrix_________________________
Difficulty: Easy		Likes: 683		Dislikes: 95		Solution: Available
Total Accepted: 91.2K		Total Submission: 152.5K		Acceptance Rate: 59.8%
Tags:  Array


In MATLAB, there is a very useful function called 'reshape', which can reshape
a matrix into a new one with different size but keep its original data.
  
You're given a matrix represented by a two-dimensional array, and two positive
integers r and c representing the row number and column number of the wanted
reshaped matrix, respectively. The reshaped matrix need to be filled with all
the elements of the original matrix in the same row-traversing order as they
were.
  
 If the 'reshape' operation with given parameters is possible and
legal, output the new reshaped matrix; Otherwise, output the original matrix.
  


Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.

"""

import itertools
def matrixReshape(nums, r, c):
	if r*c != len(nums)*len(nums[0]):    return nums
	if r==len(nums) and c==len(nums[0]):    return nums

	temp=[nums[i][j] for i in range(len(nums)) for j in range(len(nums[0]))]
	return [[*itertools.islice(temp, i*c, i*c+c)] for i in range(r)]



if __name__ == "__main__":
	nums = [[1,2,3],[4,5,6]]
	r = 1
	c = 6
	print(matrixReshape(nums,r,c,))


"""
"""
