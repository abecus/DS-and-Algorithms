from graphExamples import *
import heapq as heap


def bestFirstSearch(G, start, end, distToGoal=100):
	"""
	G: 		graph

	start: 	start node
 
	end:	end node
	
	distToGoal = heuristic for start to end distance
	"""
	if start==end:
		return end

	visited = set()			# node
	stack = []				# a heap of tuple (length form end of path to start, path(list))

	def updateHeap(dist, path):
		# updates the heap and maintains the length of to the given beam width
		heap.heappush(stack, (dist, path))

	if start in G.graph:
		# checks if start in Graph's and it has edge out from it
		visited.add(start)
		stack.append((distToGoal, [start]))

		while stack:
			print(stack)
			distToGoal, path = heap.heappop(stack)
			# find the path closest to the goal then extend the path

			node = path[-1]
			# to explore the outer node
			
			visited.add(node)
			# add to the visited set

			if node in G.graph:

				for child, length in G.graph[node].items():
					if child not in visited:
						# if node not has been visited before and 
						# can be explored further

						if child==end:
							# halts, if found the end node
							return path+[child]

						newDist = abs(distToGoal-length)
						updateHeap(newDist, path+[child])
						# updates the heap with new distance and new path

	return f"Path does not exists between the Nodes ({start} to {end})"

if __name__ == "__main__":
	graph = g4

	print(graph)
	print(' ')
	print(bestFirstSearch(graph, "s", "g", distToGoal=11))