from graphExamples import *


def connectedComponents(G):
	"takes an undirected graph"

	components={}
	visited=set()

	def findComp(node, root):		
		# if node not visited add to visited
		# and add it to it's connected components
		components[root].add(node)
		visited.add(node)

		for child, _ in G.getAdjacentNodes(node):
			if child not in visited:
				findComp(child, root)
	
	for node in G.nodes:
		if node not in visited:
			components[node]=set()
			findComp(node, root=node)
	
	return components.values()


if __name__ == "__main__":
	G=Graph()
	G.add(12, edgeType=0)
	G.add(4, [0], edgeType=0)
	G.add(8, [14, 4], edgeType=0)
	G.add(14, [13,0], edgeType=0)
	G.add(13, [0], edgeType=0)
	G.add(0, [8], edgeType=0)
	G.add(7, [6,11], edgeType=0)
	G.add(6, [7,11], edgeType=0)
	G.add(11, [7,6], edgeType=0)
	G.add(5, [17,16], edgeType=0)
	G.add(1, [5], edgeType=0)
	G.add(3, [9], edgeType=0)
	G.add(9, [15, 2], edgeType=0)
	G.add(2, [15], edgeType=0)
	G.add(15, [10], edgeType=0)
 
	print(*connectedComponents(G))
