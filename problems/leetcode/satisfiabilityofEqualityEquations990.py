"""
_________________________990. Satisfiability of Equality Equations_________________________
Difficulty: Medium		Likes: 491		Dislikes: 5		Solution: Available
Total Accepted: 18.9K		Total Submission: 42.2K		Acceptance Rate: 44.8%
Tags:  Union Find, Graph


Given an array equations of strings that represent relationships
between variables, each string equations[i] has length 4 and takes one
of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase
letters (not necessarily different) that represent one-letter variable
names. Return true if and only if it is possible to assign integers
to variable names so as to satisfy all the given equations.      


Example 1:
Input: ["a==b","b!=a"]
Output: false

Example 2:
Input: ["b==a","a==b"]
Output: true

Example 3:
Input: ["a==b","b==c","a==c"]
Output: true

Example 4:
Input: ["a==b","b!=c","c==a"]
Output: false

Example 5:
Input: ["c==c","b==d","x!=z"]
Output: true
 Note:
1 <= equations.length <= 500equations[i].length == 4equations[i][0] and equations[i][3] are lowercase lettersequations[i][1] is either '=' or '!'equations[i][2] is '='
"""


import functools, itertools, operator, bisect, array 
from typing import *

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parents = list(range(26))
        mapper = lambda x: ord(x)-ord("a")
        
        def getParent(x):
            while x != parents[x]:
                temp = parents[x]
                parents[x] = parents[temp]
                x = temp
            return x
        
        def union(x, y):
            px = getParent(x)
            py = getParent(y)
            parents[px]=py
                
        for eq in itertools.filterfalse(lambda x: x[1]=='!', equations):
            union(mapper(eq[0]), mapper(eq[-1]))
        
        for eq in itertools.filterfalse(lambda x: x[1]=='=', equations):
            if getParent(mapper(eq[0]))==getParent(mapper(eq[-1])):
                return True
        return True


if __name__ == "__main__":
    arr = ["a==b","b!=a"]    
    s = Solution()
    print(s.equationsPossible(arr))
    

"""
"""
