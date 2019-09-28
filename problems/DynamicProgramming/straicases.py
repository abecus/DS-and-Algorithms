"""
Write a function noOfStaircases(int n) that takes a positive integer n as
an input and returns the number of different staircases that can be built from
exactly n bricks. Each type of staircase should consist of 2 or more steps,
with no step being "higher" or at the same "height" than the previous one
(A step's height is equal to the total numbers of bricks that make up the step). 

All steps must contain at least one brick. 
Input format for custom testing:
An integer n representing the number of bricks.

Output format:
An integer representing the number of ways staircases can be built with exactly n bricks.
Sample testcases:

Testcase 1
Input:
3
Output    
1
Explanation:
When n=3, there is only one way to build the staircase: first step having a height of 2 and the second with a height of 1. ($ -> brick)
$
$$
Dimensions: 2x1

Testcase 2
Input:
4
Output    
1
Explanation:
When n=4, there is still only 1 way:
$
$$$
Dimensions: 3x1
Having a staircase with dimensions 2x2 is invalid since both the steps would be at the same height. 


Testcase 3
Input:
5
Output    
2
Explanation:
But when n=5. there are 2 ways with dimensions 3x2 and 4x1, as listed below:
1st way
$$
$$$
2nd way
$
$$$$
"""

def nStairs(n, k):
    mem = [[-1 for _ in range(n+2)] for _ in range(n+2)]
    mem[0][0] = 1
    
    def helper(n, k):
        if mem[n][k]!=-1:
            return mem[n][k]
        
        if n==0:
            return 1
        
        if k>n:
            return 0
            
        mem[n][k] = helper(n-k, k+1) + helper(n, k+1)
        return mem[n][k]
    
    return helper(n, k)

# for i in range(1, 6):
#     print(nStairs(i, 1))
print(nStairs(500, 1))