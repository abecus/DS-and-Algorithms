"""
_________________________207. Course Schedule_________________________
Difficulty: Medium		Likes: 3601		Dislikes: 170		Solution: Available
Total Accepted: 399K		Total Submission: 940.3K		Acceptance Rate: 42.4%
Tags:  Graph, Breadth-first Search, Topological Sort, Depth-first Search


There are a total of numCourses courses you have to take, labeled from
0 to numCourses-1. Some courses may have prerequisites, for example
to take course 0 you have to first take course 1, which is expressed
as a pair: [0,1] Given the total number of courses and a list of
prerequisite pairs, is it possible for you to finish all courses?   


Example 1:Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
             To take course 1 you should have finished course 0. So it is possible.
Example 2:Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
             To take course 1 you should have finished course 0, and to take course 0 you should             also have finished course 1. So it is impossible. The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
"""

import collections

def canFinish(numCourses, prerequisites):
	g=collections.defaultdict(set)
	for i,j in prerequisites:
		if i in g[j]:   return 0
		g[i].add(j)
	
	print(*g.items(), sep='\n')
	
	def dfs(i, seen):
		if i in visited:	return 1
		if i in seen:	return 0

		res=1
		for j in g[i]:
			seen.add(i)
			res = res and dfs(j, seen)
			if not res:
				return res

		visited.add(i)
		return res
	
	visited=set()
	for i in g:
		if not dfs(i, set()):
			return 0
	return 1


if __name__ == "__main__":
	numCourses = 	2
	prerequisites = [[1,0]]
	# numCourses = 8 	
	# prerequisites = [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]
	print(canFinish(numCourses,prerequisites,))


"""
similarQuestions::
		Course Schedule II: Medium
		Graph Valid Tree: Medium
		Minimum Height Trees: Medium
		Course Schedule III: Hard
"""
