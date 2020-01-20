from graphExamples import *
from unionFind import UnionFind


def kruskal(G)-> "list(namedetuple)":
	res = []
	u = UnionFind()	# initialise union-find DS

	for edge in iter(sorted(G.edges, key=lambda x: x.weight)):
		# go through all the edges and feed the nodes to the union method
		# if their roots are not same
		if u.isConnected(edge.node1, edge.node2):	continue
		u.union(edge.node1, edge.node2)
		res.append(edge)
	return res

if __name__ == "__main__":
	G = g2
	print(*kruskal(G))