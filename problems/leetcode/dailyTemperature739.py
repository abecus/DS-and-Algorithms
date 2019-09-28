"""
739. Daily Temperatures
Given a list of daily temperatures T, return a list 
such that, for each day in the input, tells you how 
many days you would have to wait until a warmer 
temperature. If there is no future day for which this 
is possible, put 0 instead.

For example, given the list of temperatures 
T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range 
[1, 30000]. Each temperature will be an integer in 
the range [30, 100].
"""


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        l = len(T)
        res = [0 for x in range(l)]
        s=[]
        popper = s.pop
        appender = s.append
        for i in range(l):
            while s and T[s[-1]] < T[i]:
                idx = popper()
                res[idx]= i - idx
            
            appender(i)
        
        return res  
                    