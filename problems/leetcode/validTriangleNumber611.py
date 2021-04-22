"""
_________________________611. Valid Triangle Number_________________________
Difficulty: Medium		Likes: 1119		Dislikes: 95		Solution: Available
Total Accepted: 67.2K		Total Submission: 138.4K		Acceptance Rate: 48.5%
Tags:  Array


Given   an   array   consists   of   non-negative   integers,     your  task  is
to   count   the   number   of   triplets   chosen   from  the  array  that  can
make triangles if we take them as side lengths of a triangle.
									

																																							 
																																								


Example 1: 
 Input: [2,2,3,4]
 Output: 3
 2,3,4 (using the first 2)
 2,3,4 (using the second 2)
 2,2,3
	 Note:
	The length of the given array won't exceed 1000.
 The integers in the given array are in the range of [0, 1000].
	 
"""


import functools
import itertools
import operator
import bisect
import array
import collections
from typing import *


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)-2):
            k = i+2
            for j in range(i+1, len(nums)-1):
                while k < len(nums) and nums[i]+nums[j] > nums[k]:
                    k += 1
                res += k-j-1
        return res


if __name__ == "__main__":
    A = [2, 2, 3, 4]
    s = Solution()
    print(s.triangleNumber(A))


"""
similarQuestions::
		3Sum Smaller: Medium
"""
