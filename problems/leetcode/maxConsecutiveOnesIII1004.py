"""
_________________________1004. Max Consecutive Ones III_________________________
Difficulty: Medium		Likes: 1132		Dislikes: 24		Solution: Available
Total Accepted: 57.5K		Total Submission: 97.7K		Acceptance Rate: 58.9%
Tags:  Two Pointers, Sliding Window


Given an array A of 0s and 1s, we may change up to K values from 0 to 1. Return
the length of the longest (contiguous) subarray that contains only 1s.     


Example 1:
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Example 2:
Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
 Note:
1 <= A.length <= 200000 <= K <= A.lengthA[i] is 0 or 1 

"""


import functools, itertools, operator, bisect, array
from typing import *

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i = j = zs = res = 0
        while j<len(A):
            zs += A[j]==0
            while zs>K:
                zs -= A[i]==0
                i+=1
            res = max(res, j-i+1)
            j+=1
        return res
        


if __name__ == "__main__":
	s = Solution()
	print(s.longestOnes(A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3))


"""
similarQuestions::
		Longest Substring with At Most K Distinct Characters: Hard
		Longest Repeating Character Replacement: Medium
		Max Consecutive Ones: Easy
		Max Consecutive Ones II: Medium
"""
