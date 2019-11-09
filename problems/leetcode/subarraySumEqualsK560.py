"""
_________________________560. Subarray Sum Equals K_________________________
Difficulty: Medium		Likes: 2557		Dislikes: 71		Solution: Available
Total Accepted: 146.9K		Total Submission: 341.7K		Acceptance Rate: 43.0%
Tags:  Array, Hash Table


Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
Example 1:

Input:nums = [1,1,1], k = 2
Output: 2


Note:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


"""


def subarraySum(nums, k):
    d = {}
    d[0] = 1
    s = 0
    res = 0
    
    for i in nums:
        s+=i
        res+=d.get(s-k, 0)
        d[s]=d.get(s, 0)+1
    return res

if __name__ == "__main__":
    nums = [1,1,1]
    k = 2
    
    nums = [2,-4,1,6,-2]
    k = 3
    print(subarraySum(nums,k,))


"""
similarQuestions::
        Two Sum: Easy
        Continuous Subarray Sum: Medium
        Subarray Product Less Than K: Medium
        Find Pivot Index: Easy
        Subarray Sums Divisible by K: Medium
"""
