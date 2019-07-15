"""
62. Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach 
the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28
"""

import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    
    i = reduce(op.mul, range(n, n-r, -1), 1)
    j = reduce(op.mul, range(1, r+1), 1)
    return i / j

def foo(m, n):
    return int(ncr(m+n-2, min(n-1, n-1)))

print(foo(7, 3))
