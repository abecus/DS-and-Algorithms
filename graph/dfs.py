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

	visited = set()
	path = []
 
	def helper(node):
		if node == end:
			# found the end node
			return node

		visited.add(node)
		# add node to visited
  
		if node in G.graph:
			for child in G.graph[node]:
				# looping through all node which are 
				# connected by edges

				if child not in visited:
					# if nodes are not visited before explore

					if helper(child)!=None:
						path.append(child)
						return path
	
	if start in G.graph:
		path = helper(start)
		visited.add(start)
		path.append(start)
		
		if path != None:
			# if path has been found return it
			return [*reversed(path)]

	return f"Path does not exists between the Nodes ({start} to {end})"

if __name__ == "__main__":
    
	print(dfs(g5, "s", "g"))