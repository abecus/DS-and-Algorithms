"""
_________________________698. Partition to K Equal Sum Subsets_________________________
Difficulty: Medium		Likes: 1245		Dislikes: 70		Solution: Available
Total Accepted: 65.3K		Total Submission: 147.1K		Acceptance Rate: 44.4%
Tags:  Recursion, Dynamic Programming


Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
 
Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

 
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.

"""

import functools

def canPartitionKSubsets(nums, k):
    
    if k==1:   return 1
    
    s=sum(nums)
    target=s//k

    if target*k != s:
        return 0

    nums.sort()
    if nums[-1]>target: return 0
 
    while nums and nums[-1]==target:
        nums.pop()
        k-=1
  
    @functools.lru_cache(None)
    def foo(i,k,t):
        if t<0:		return 0
        
        if k==0:	return 1

        if t==0:	return foo(0,k-1,target)

        for j in range(i,len(nums)):
            if j in s: continue
            s.add(j)				
            if foo(i+1, k, t-nums[j]):  return 1
            s.discard(j)
        return 0

    s=set()
    nums.reverse()
    return foo(0,k,target)

if __name__ == "__main__":
    nums = [4,3,2,3,5,2,1]
    k = 4
    print(canPartitionKSubsets(nums,k,))


"""
similarQuestions::
        Partition Equal Subset Sum: Medium
"""
