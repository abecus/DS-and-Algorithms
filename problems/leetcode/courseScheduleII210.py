"""
_________________________210. Course Schedule II_________________________
Difficulty: Medium		Likes: 2186		Dislikes: 130		Solution: Available
Total Accepted: 261.2K		Total Submission: 657.3K		Acceptance Rate: 39.7%
Tags:  Breadth-first Search, Topological Sort, Graph, Depth-first Search


There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you
have to first take course 1, which is expressed as a pair: [0,1] Given
the total number of courses and a list of prerequisite pairs, return
the ordering of courses you should take to finish all courses. There
may be multiple correct orders, you just need to return one of them.
If it is impossible to finish all courses, return an empty array.


Example 1:
Input: 2, [[1,0]]
Output: [0,1]
             course 0. So the correct course order is [0,1] .
Example 2:
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

"""


import functools, itertools, operator, bisect, array, collections
from typing import *


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.is_possible = 1
        g = collections.defaultdict(list)
        for t, f in prerequisites:
            g[f].append(t)

        def foo(node):
            if self.is_possible == 0:   return

            seen[node] = 1
            for adj in g.get(node, []):
                if seen[adj]==0:
                    foo(adj)
                elif seen[adj]==1:
                    self.is_possible = 0
                    break
                    
            res.append(node)
            seen[node]=2

        res=[]
        seen=[0]*numCourses
        for course in range(numCourses):
            if seen[course]==0:
                foo(course)
                
        return [] if not self.is_possible else res[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.findOrder(5, [[1,0],[2,0],[3,1],[3,2], [0, 4]]))


"""
similarQuestions::
		Course Schedule: Medium
		Alien Dictionary: Hard
		Minimum Height Trees: Medium
		Sequence Reconstruction: Medium
		Course Schedule III: Hard
"""
