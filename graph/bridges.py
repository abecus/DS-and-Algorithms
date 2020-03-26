from graphExamples import *
from collections import defaultdict


def bridges(G: "graph"):
	# takes an undirected graph

	def helper(at, parent, i):
		ids[at]=llVal[at]=i
		i+=1

		for node, _ in G.getAdjacentNodes(at):
			if node==parent:
				# makes sure that every edge is directed
				continue
		
			if ids[node]==0:
				# if node have more been visited before explore it
				helper(node, at, i)

				# updates the low link val of "at" node in call back
				llVal[at]=min(llVal[node], llVal[at])

				if ids[at]<llVal[node]:
					# if above condition meets its an bridge
					bridges.append((at, node))
			else:
				# if node nas been visited before and check if lowLink val
				# of "at" node can be updated
				llVal[at] = min(llVal[at], ids[node])

		return i
	
	ids = defaultdict(lambda: 0)
	llVal = {}
	bridges = []
	i=1
	for node in G.nodes:
		if ids[node]==0: # if node not been visited
			i=helper(at=node, parent=-1, i=i)

	return bridges
	
if __name__ == "__main__":
	G = g14
	# G = Graph()
	# G.addFromDict(0, {1:4, 2:1})
	# G.addFromDict(1, {3:1})
	# G.addFromDict(2, {1:2, 3:5})
	# G.addFromDict(3, {4:3})
	print(bridges(G))