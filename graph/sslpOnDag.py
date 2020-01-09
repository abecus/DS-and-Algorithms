from graphExamples import *
from topologicalOrder import topologicalSort
from collections import defaultdict


def singleSourceLongestPathOnDag(G, startingNode):
	"""
	itype:	G(Graph),	startingNode(a node of graph G)

	rtype: parentsDict(dict), nodeCosts(dict)
	"""
	def dfs(node, root):
		for adjNode, weight in G.getAdjcentNodes(node):
			# loop through all the adjcent-nodes of the graph-node (node)
			# and change edge weights sign and find sortest path
			weight *= -1

			newCost = weight + nodeCosts[node]
			# cost to the adjNode from "node" using best cost in the nodeCosts dict
			if nodeCosts[adjNode]>newCost:
				# update cost of adjNode if its more than the newCost
				# and update the parent dict by (adjcent:node)
				nodeCosts[adjNode] = newCost
				parents[adjNode] = node
				
	parents = {}
	# to reconstruct the path to the end node from starting Node
 
	nodeCosts = defaultdict(lambda: float('inf'))
	# nodeCosts retains the cost to the nodes from startingNode
 
	nodeCosts[startingNode] = 0
	# initialise the nodeCosts value of the startingNode
	
	for node in topologicalSort(G):
		# run the dfs for all the nodes in topological order
		dfs(node, root=node)

	return parents, nodeCosts

if __name__ == "__main__":
	G=g7
	# print(dir(g7))
	parentsDict, nodeCosts = singleSourceLongestPathOnDag(G, startingNode="a")
	print(*nodeCosts.items())
	print(parentsDict)