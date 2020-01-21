# As a stand-alone, generally used to find if node exists in the graph, and to 
# find a path to it

from graphExamples import *

def dfs(G, start, end):
	"""
	G: 		graph
 
	start: 	start node
 
	end:	end node
	"""
	if start==end:
		return end
 
	def helper(node, path):
		if node == end:
			# found the end node
			return node

		visited.add(node)
		# add node to visited

		for child, _ in G.getAdjcentNodes(node):
			# looping through all node which are 
			# connected by edges

			if child not in visited:
				# if nodes are not visited before explore

				if helper(child, path)!=None:
					path.append(child)
					return path

	
	visited = set()
	path = []
	if start in G.graph:
		path = helper(start, path)
		
		if path != None:
			# if path has been found return it
			return [*reversed(path+[start])]

	return f"Path does not exists between the Nodes ({start} to {end})"

if __name__ == "__main__":
    
	print(dfs(g6, "a", "m"))