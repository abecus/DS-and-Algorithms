from graphExamples import *
import heapq as heap


def aStar(G, start, end):
	"""
	G: 		graph with admissable heuristic

	start: 	start node
 
	end:	end node
	
	distToGoal = heuristic for start to end distance
	"""
	if start==end:
		return end

	visited = set()			# node
	stack = []				# a heap of tuple (length form end of path to start, path(list))

 
	def getPath():
		"""
		returns the top path 
		"""
		pass
		
	def updateHeap(dist, path):
		# updates the heap and maintains the length of to the given beam width
		heap.heappush(stack, (dist, path))

	if start in G.graph:
		# checks if start in Graph's and it has edge out from it
		visited.add(start)
		stack.append((G.getHeuristic(start, end), [start]))

		while stack:
			print(stack)
			dist, path = heap.heappop(stack)
			# find the path closest to the goal then extend the path

			node = path[-1]
			# to explore the outer node

			if node==end:
				# halts, if found the end node
				return path

			visited.add(node)
			# add to the visited set

			if node in G.graph:

				for child, length in G.graph[node].items():
					if child not in visited:
						# if node not has been visited before and 
						# can be explored further

						childAdmHeuristic = G.getHeuristic(child, end) if child!=end else 0
						nodeAdmHeuristic = G.getHeuristic(node, end)

						newAccumulatedDist = dist+length-nodeAdmHeuristic+childAdmHeuristic
						updateHeap(newAccumulatedDist, path+[child])
						# updates the heap with new distance and new path

	return f"Path does not exists between the Nodes ({start} to {end})"

if __name__ == "__main__":
	graph = g4	 
	g4.addHeuristicFromDict("s", {"g": 10.5})
	g4.addHeuristicFromDict("a", {"g": 7.5})
	g4.addHeuristicFromDict("b", {"g": 6})
	g4.addHeuristicFromDict("c", {"g": 7.5})
	g4.addHeuristicFromDict("g", {"g": 0})
	g4.addHeuristicFromDict("e", {"g": 5})
	g4.addHeuristicFromDict("d", {"g": 5})

	print(graph)
	print(' ')
	path = aStar(graph, "s", "g")
	print(path, g4.getCost(path))
