from graphExamples import *
from collections import defaultdict


def articulationPoints(G: "graph"):
	# takes an undirected graph

	def helper(root, at, parent, i):
		outEdge=0
		ids[at]=llVal[at]=i
		i+=1

		for node, _ in G.getAdjacentNodes(at):
			if node==parent:
				# makes sure that every edge is directed
				continue
		
			if ids[node]==0:
				outEdge+=1

				# if node have not been visited before, explore it
				i = helper(root=root, at=node, parent=at, i=i)

				# updates the low link val of "at" node in call back
				llVal[at] = min(llVal[node], llVal[at])

				if (ids[at]<=llVal[node] and parent!=-1) or (outEdge>1 and parent==-1):
					# If at is not root and low value of one of its child is more than index value of at.
					# OR
					# at is root of DFS tree and has two or more children. 
					artPoints.add(at)

			else:
				# if node nas been visited before and check if lowLink val
				# of "at" node can be updated
				llVal[at] = min(llVal[at], ids[node])

		return i
	
	ids = defaultdict(lambda: 0)
	llVal = {}
	artPoints = set()
	i=1
	for node in G.nodes:
		if ids[node]==0:	# if node not been visited
			i = helper(root=node, at=node, parent=-1, i=i)
	return artPoints
	
if __name__ == "__main__":
	G = g14
	G = Graph()
	G.addFromDict(0, {1:4, 2:1})
	G.addFromDict(1, {3:1})
	G.addFromDict(2, {1:2, 3:5})
	G.addFromDict(3, {4:3})
	print(articulationPoints(G))
 