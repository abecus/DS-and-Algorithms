"""
_________________________665. Non-decreasing Array_________________________
Difficulty: Easy		Likes: 1261		Dislikes: 293		Solution: Available
Total Accepted: 65.4K		Total Submission: 336K		Acceptance Rate: 19.5%
Tags:  Array



Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.


We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:

Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.


Example 2:

Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.


Note:
The n belongs to [1, 10,000].
"""


def checkPossibility(nums):

    l = len(nums)
    i = 1
    while i<l and nums[i-1]<=nums[i]:
        i+=1
    i-=1
    j=l-2
    while j>i and nums[j+1]>=nums[j]:
        j-=1
    j+=1
    
    if j-i>=2:
        return False
    if i:
        if l-1!=j:
            if nums[i]<=nums[j+1] or nums[i-1]<=nums[j]:
                return True
            return False
        print
        return True
    if j-i>1:
        return False
    return True

if __name__ == "__main__":
    nums = [
            [4,2,3],  #1
            [4,2,1],  #0
            [4,2],    #1
            [4,2,5],  #1
            [3,4,2,3], #0
            [3,4,2,5,1], #0
            [1,5,4,6,7,10,8,9], #0
            [1,2,5,4,3] #0
    ]
    
    for i in nums:
        print(checkPossibility(i))


"""
"""
