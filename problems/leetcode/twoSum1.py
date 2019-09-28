"""
_________________________1. Two Sum_________________________
Difficulty: Easy		Likes: 11865		Dislikes: 409		Solution: Available
Total Accepted: 2.1M		Total Submission: 4.8M		Acceptance Rate: 44.5%
Tags:  Array, Hash Table


Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:


Given nums = [2, 7, 11, 15], target = 9,



Because nums[0] + nums[1] = 2 + 7 = 9,

return [0, 1].


"""


def twoSum(nums, target):
    d = {}
    for i, ele in enumerate(nums):
        if ele in d:
            return [d[ele], i]
        else:
            d[target-ele]=i


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums,target,))


"""
similarQuestions::
        3Sum: Medium
        4Sum: Medium
        Two Sum II - Input array is sorted: Easy
        Two Sum III - Data structure design: Easy
        Subarray Sum Equals K: Medium
        Two Sum IV - Input is a BST: Easy
        Two Sum Less Than K: Easy
"""
