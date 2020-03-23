"""
_________________________1042. Flower Planting With No Adjacent_________________________
Difficulty: Easy		Likes: 216		Dislikes: 270		Solution: None
Total Accepted: 18.8K		Total Submission: 38.9K		Acceptance Rate: 48.2%
Tags:  Graph


You have N gardens, labelled 1 to N.  In each garden, you want to plant
one of 4 types of flowers. paths[i] = [x, y] describes the existence of a
bidirectional path from garden x to garden y. Also, there is no garden that has
more than 3 paths coming into or leaving it. Your task is to choose a flower
type for each garden such that, for any two gardens connected by a path, they
have different types of flowers. Return any such a choice as an array answer,
where answer[i] is the type of flower planted in the (i+1)-th garden.  The
flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.    


Example 1:
Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]

Example 2:
Input: N = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]

Example 3:
Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
 Note:
1 <= N <= 100000 <= paths.size <= 20000No garden has 4 or more paths coming into or leaving it.
It is guaranteed an answer exists.

"""

from collections import defaultdict
def gardenNoAdj(N, paths):
	# create a graph to show the path b/w the gardens
	g=defaultdict(set)
	
	# set to represent all the flowers
	flowers=set((1,2,3,4))

	# add edges to the graph
	for i,j in paths:
		g[i].add(j)
		g[j].add(i)

	# array to store the results
	res=[0]*N

	# loop for all the gardens
	for i in range(1, N+1):

		# get all the flower given to other gardens if
		# there is path between the garden_i and the other 
		# garden_to and store into givenFlowerset
		givenFlower=set()
		for to in g[i]:
			if res[to-1]:
				givenFlower.add(res[to-1])

		# take any flower(using pop() method)
		# from the available ones
		res[i-1]=(flowers-givenFlower).pop()

	# return the res array
	return res


if __name__ == "__main__":
	# 5
	# [[4,1],[4,2],[4,3],[2,5],[1,2],[1,5]]
	# [1,2,1,3,3]

	# N = 3
	# paths = [[1,2],[2,3],[3,1]]

	N=5
	paths = [[4,1],[4,2],[4,3],[2,5],[1,2],[1,5]]
 
	# N = 4
	# paths = [[1,2],[3,4]]
 
	# N = 4
	# paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
	print(gardenNoAdj(N,paths,))


"""
"""
