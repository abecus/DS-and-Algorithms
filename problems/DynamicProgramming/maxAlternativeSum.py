"""
Given an array of integers, find the subset of non-adjacent elements with the maximum sum.
Calculate the sum of that subset.

For example, given an array "arr=[-2, 1, 3, -4, 5]"  we have the following possible subsets:

Subset      Sum
[-2, 3, 5]   6
[-2, 3]      1
[-2, -4]    -6
[-2, 5]      3
[1, -4]     -3
[1, 5]       6
[3, 5]       8

Our maximum subset sum 8 is.
"""

def maxSubsetSum(arr):
    """
    finds maximum non adjecent sum in arr
    
    ityp: list
    rtype: int
    """
    inc = max(0, arr[0])
    exc = 0

    for i in range(1, len(arr)):
        
        s = arr[i] + exc
        temp = inc
        
        if s>inc:
            inc = s
            
        exc = temp

    return inc