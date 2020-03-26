import heapq as heap
from graphExamples import *
from collections import namedtuple



# explore greedily (using the nodes which are closer to goal) in dfs manner.
def hillClimbing(G, start, end, distToGoal=100):
	"""
	G:		graph
 
	start:	start node
 
	end:	end node
	
	distToGoal = heuristic for start to end distance
	"""
	if start==end:
		return end

	Node = namedtuple("Node", ("goalDist", "node"))
	visited = set()

	def helper(at, path, covered):
		if at==end:
			return at

		visited.add(at)

		tempStack = []		# temp heap to keep the at's adjacent nodes
		for node, length in G.getAdjacentNodes(at):
			if node in visited:	continue
			covered += length
			heap.heappush(tempStack, Node(goalDist=abs(distToGoal-covered), node=node))
			covered-=length

		while tempStack:
			minNode=heap.heappop(tempStack)

			if helper(minNode.node, path, minNode.goalDist):
				path.append(minNode.node)
				return path

	if start in G.graph:
		path = helper(start, [], 0)

		if path != None:
			# if path has been found return it
			return [*reversed(path+[start])]

	return f"Path does not exists between the Nodes ({start} to {end})"

if __name__ == "__main__":
	print(g4)
	# print(' ')
	print(hillClimbing(g4, "s", "g", distToGoal=11))
