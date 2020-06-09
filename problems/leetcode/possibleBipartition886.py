"""
_________________________886. Possible Bipartition_________________________
Difficulty: Medium		Likes: 860		Dislikes: 27		Solution: Available
Total Accepted: 51.8K		Total Submission: 118.9K		Acceptance Rate: 43.6%
Tags:  Depth-first Search


Given a set of N people (numbered 1, 2, ..., N), we would like to split
everyone into two groups of any size. Each person may dislike some
other people, and they should not go into the same group.  Formally,
if dislikes[i] = [a, b], it means it is not allowed to put the people
numbered a and b into the same group. Return true if and only if it
is possible to split everyone into two groups in this way.          


Example 1:Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true

Example 2:Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
 1 <= N <= 20000 <= dislikes.length <= 10000dislikes[i].length == 21 <= dislikes[i][j] <= Ndislikes[i][0] < dislikes[i][1]There does not exist i != j for which dislikes[i] == dislikes[j].

"""

import functools, collections

def possibleBipartition(N, dislikes):
	g=collections.defaultdict(set)
	for i,j in dislikes:
		g[i].add(j)
		g[j].add(i)
 
	def foo(i, c):
		if color[i]==c^1:	return 0
		if color[i]!=None:	return 1
		
		color[i]=c
		for j in g[i]:
			if not foo(j,c^1):	return 0
		return 1
      
	color=[None]*(N+1)
	for i in range(1,N+1):
		if color[i]!=None:		continue
		if not foo(i,0):	return 0
	return 1
		
if __name__ == "__main__":
	# N = 4; dislikes = [[1,2],[1,3],[2,4]]  #1
	# N = 3; dislikes = [[1,2],[1,3],[2,3]]  #0
	# N = 5; dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]  #0
	N=10; dislikes=[[1,2],[3,4],[5,6],[6,7],[8,9],[7,8]]  #1
	print(possibleBipartition(N,dislikes,))


"""
"""
