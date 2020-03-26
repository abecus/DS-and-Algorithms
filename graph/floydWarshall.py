from graphExamples import *
from collections import defaultdict

def floydWarshall(G):
	"""
	itype:	G(Graph)

	rtype: parentsDict(dict), allCosts(dict)
	"""
	def isEdgeBetweenNodes(parentNode, node):
		"rtype: boolean"
		return parentNode in dp and node in dp[parentNode]
 
	# get all the nodes of the graph
	nodes = [*G.nodes]

	# keeps the costs among the all nodes
	dp = defaultdict(lambda: defaultdict(lambda: float('inf')))

	# for path reconstruction 
	parents = defaultdict(lambda: defaultdict(lambda: 0))

	for node in nodes:
		# cost from a node to same node
		dp[node][node] = 0
 
	for parentNode, node, weight in G.edges:
		# initialise the parent and dp dictionary
		dp[parentNode][node] = weight
		parents[parentNode][node] = node

	for middleNode in nodes:
		for firstNode in nodes:
			for lastNode in nodes:
				# loop through all the possible path to through all possible nodes

				# cost from firstNode-middleNode + middleNode-lastNode
				newCost = dp[firstNode][middleNode]+dp[middleNode][lastNode]

				if newCost < dp[firstNode][lastNode]:
					# update cost if new lower cost path has been found
					dp[firstNode][lastNode] = newCost

					# update the parentDict for path reconstruction
					parents[firstNode][lastNode] = parents[firstNode][middleNode]
	
	return parents, dp
		


if __name__ == "__main__":
	G = g8
	# print(G)
	# print(' ')

	parentDict, allCosts = floydWarshall(G)
	for k, v in allCosts.items():
		print(k, dict(v))

	# print(' ')
	# for k, v in parentDict.items():
	# 	print(k, dict(v))
	