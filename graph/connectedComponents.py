from graphExamples import *

def connectedComponents(graph):
	
	components={}
	visited=set()
	def findComp(node, root):
		if node not in visited:
			components[root].add(node)
			visited.add(node)

			if node in graph:
				for child in graph[node]:
					findComp(child, root)
	
	for node in graph.keys():
		if node not in visited:
			components[node]=set()
			findComp(node, root=node)
	
	return components

if __name__ == "__main__":
	print(connectedComponents(graph1))