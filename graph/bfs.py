# As a stand-alone, generally used to find if node exists 
# in the graph, and to find a path to it

from graphExamples import *
from collections import deque


def bfs(G, start, end):
	"""
	G: 		graph
 
	start: 	start node
 
	end:	end node
	"""
	visited = set()
	parent = {}
	queue = deque([])
	dequeSet = set()

	def backtrace(parent=parent, start=start, end=end):
		path = [end]
		while path[-1] != start:
			path.append(parent[path[-1]])
   
		return " --> ".join(map(str, reversed(path)))

	if start in G.graph:
		# checks if start in Graph's and it has edge out from it
		visited.add(start)
		queue.append(start)
		dequeSet.add(start)
		
		while queue:
			# until their is something to explore in queue
			# take node to explore from front of queue
			node = queue.popleft()
			dequeSet.remove(node)
								
			if node==end:
				# halts, if found the end node
				return backtrace()
			
			visited.add(node)
			# add to the visited

			if node in G.graph:
				for child in G.graph[node]:
					if not (child in visited or child in dequeSet):
						# if node not has been visited before and 
						# can be explored further

						parent[child]=node
						# updating parent dictionary

						queue.append(child)
						dequeSet.add(child)
	
	return f"Path does not exists between the Nodes ({start} to {end})"

if __name__ == "__main__":
	# print(g5)
	print(bfs(g5, "s", "g"))
