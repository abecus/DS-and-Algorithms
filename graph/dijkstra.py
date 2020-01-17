from graphExamples import *
from topologicalOrder import topologicalSort
from collections import defaultdict
import heapq as heap
from tree.indexedPriorityQueue import IndexedPriorityQueue


def dijkstra(G, startingNode):
	"""
	itype:	G(Graph),	startingNode(a node of graph G)

	rtype: parentsDict(dict), nodeCosts(dict)
	"""

	# to reconstruct the path to the end node from starting Node
	parents = {}
 
	# to keep the keys of nodes in the heap
	pqKeyMap = {}

	# to keep track of visited nodes
	visited = set()
 
	# contains which node to visit first based on cost to the node
	pq = IndexedPriorityQueue([])

	# nodeCosts retains the cost to the nodes from startingNode
	nodeCosts = defaultdict(lambda: float('inf'))
 
	# initialise the nodeCosts value of the startingNode
	# and priority queue to the 0 cost of startingNode
	# also add the starting node to the parents dict for visited tag
	nodeCosts[startingNode] = 0
	pq.push((0, startingNode))
	pqKeyMap[startingNode] = pq.arrSize-1

	# while priorityQueue:
	while pq.heapSize:
		# go greedily by always extending the shorter cost nodes first
		_, node = pq.pop()
		del pqKeyMap[node]

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

				if adjNode in pqKeyMap:
					pq.update(pqKeyMap[adjNode], (newCost, adjNode))
				else:
					pq.push((newCost, adjNode))
					pqKeyMap[adjNode] = pq.arrSize-1

	return parents, nodeCosts

if __name__ == "__main__":
	G=g9
	# print(G)
	parentsDict, nodeCosts = dijkstra(G, startingNode=0)
	print(*nodeCosts.items())
	print(parentsDict)
