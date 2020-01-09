from graphExamples import *
from topologicalOrder import topologicalSort
from collections import defaultdict
import heapq as heap


def dijkstra(G, startingNode):
	"""
	itype:	G(Graph),	startingNode(a node of graph G)

	rtype: parentsDict(dict), nodeCosts(dict)
	"""

	# to reconstruct the path to the end node from starting Node
	parents = {}

	# to keep track of visited nodes
	visited = set()
 
	# contains which node to visit first based on cost to the node
	priorityQueue = []

	# nodeCosts retains the cost to the nodes from startingNode
	nodeCosts = defaultdict(lambda: float('inf'))
 
	# initialise the nodeCosts value of the startingNode
	# and priority queue to the 0 cost of startingNode
	# also add the starting node to the parents dict for visited tag
	nodeCosts[startingNode] = 0
	heap.heappush(priorityQueue, (0, startingNode))

	while priorityQueue:
		# go greedily by always extending the shorter cost nodes first
		w, node = heap.heappop(priorityQueue)

		if w>nodeCosts[node]:
			# if node with shorter path is also available continue
			continue

		visited.add(node)

		for adjNode, weight in G.getAdjcentNodes(node):
			# loop through all the adjcent nodes

			if adjNode in visited:
				continue

			newCost = nodeCosts[node]+weight
			if nodeCosts[adjNode] > newCost:
				# update new cost if its their from the "node" to "adjNode"
				parents[adjNode]=node
				nodeCosts[adjNode]=newCost
				heap.heappush(priorityQueue, (newCost, adjNode))

	return parents, nodeCosts

if __name__ == "__main__":
	G=g11
	# print(G)
	parentsDict, nodeCosts = dijkstra(G, startingNode=0)
	print(*nodeCosts.items())
	print(parentsDict)
