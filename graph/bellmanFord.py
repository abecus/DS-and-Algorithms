from graphExamples import *
from collections import defaultdict


def belmanFord(G, startingNode):
	"""
	itype:	G(Graph),	startingNode(a node of graph G)

	rtype: parentsDict(dict), nodeCosts(dict), nNodes(int)
	"""
	nNodes = len(list(G.nodes))

	# to reconstruct the path to the end node from starting Node
	parents = {}

	# nodeCosts retains the cost to the nodes from startingNode
	nodeCosts = defaultdict(lambda: float('inf'))
 
	# initialise the nodeCosts value of the startingNode
	nodeCosts[startingNode] = 0

	for _ in range(nNodes):
		for parentNode, node, weight in G.edges:
			newCost = nodeCosts[parentNode]+weight

			if newCost < nodeCosts[node]:
				nodeCosts[node] = newCost
				parents[node] = parentNode

	return parents, nodeCosts, nNodes

def detectNegativeCycle(nodeCosts, nNodes):
	# run main loop again and find change in nodeCosts dict
	# if change occurs tag it as effected node by negative cycles
	for _ in range(nNodes):
		for parentNode, node, weight in G.edges:
			if nodeCosts[parentNode] + weight < nodeCosts[node]:
				nodeCosts[node] = -float('inf')

	return nodeCosts


if __name__ == "__main__":
	G=g11
	print(G.description)
	parentsDict, nodeCosts, nNodes = belmanFord(G, startingNode=0)
	nodeCosts = detectNegativeCycle(nodeCosts, nNodes)
	print(*nodeCosts.items())
	print(parentsDict)