from graphExamples import *
from unionFind import UnionFind


def connectedComponentsUF(G):
	# works on both directed and undirected graphs

	u=UnionFind()	# initialise union-find DS

	for edge in G.edges:
		# go through all the edges and feed the nodes to the union method
		u.union(edge.node1, edge.node2)

	for node in G.nodes:
		# go through all nodes and finalize the roots of all the remaining nodes
		u.find(node)

	# return  the rootMap of the nodes
	return u.parentsMap
 
if __name__ == "__main__":
	G = g1
	print(*connectedComponentsUF(G).items())