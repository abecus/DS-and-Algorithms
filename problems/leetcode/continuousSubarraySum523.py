"""
_________________________523. Continuous Subarray Sum_________________________
Difficulty: Medium		Likes: 1253		Dislikes: 1751		Solution: Available
Total Accepted: 123.3K		Total Submission: 504K		Acceptance Rate: 24.5%
Tags:  Math, Dynamic Programming


Given a list of non-negative numbers and a target integer k, write a function
to check if the array has a continuous subarray of size at least 2 that sums
up to a multiple of k, that is, sums up to n*k where n is also an integer.   


Example 1:Input: [23, 2, 4, 6, 7],  k=6
Output: True

Example 2:Input: [23, 2, 6, 4, 7],  k=6
Output: True
 The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

"""


import functools, itertools, operator, bisect, array 

class Solution:
    def checkSubarraySum(self, nums: list, k: int) -> bool:
        
        stack=[(sum(nums), 0, len(nums)-1)]

        while stack:
            s,i,j=stack.pop()

            if s%k==0:
                return 1

            if i<j:
                stack.append((s-nums[i], i+1, j))
                stack.append((s-nums[j], i, j-1))
            
        return 0
    
        def foo(s,i,j):
            if j-i>1:
                return False
            if s%k==0:
                return True
            
            return any(foo(s-nums[i], i+1, j), foo(s-nums[j], i, j-1))

        return foo(sum(nums), 0, len(nums)-1)


if __name__ == "__main__":
    nums=[23, 2, 4, 6, 7]
    k=6
    
    nums = [23, 2, 6, 4, 7]
    k=6

    s=Solution()
    print(s.checkSubarraySum(nums, k))


"""
similarQuestions::
        Subarray Sum Equals K: Medium
"""
