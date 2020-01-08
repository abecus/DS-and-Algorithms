from graphExamples import *
from collections import deque

def hillClimbing(G, start, end, distToGoal=100):
	"""
	G:		graph
 
	start:	start node
 
	end:	end node
	
	distToGoal = heuristic for start to end distance
	"""
	if start==end:
		return end

	visited = set()			# node
	stack = deque()			# doubly linked list used to reduce the item removal complexity

	if start in G.graph:
		# checks if start in Graph's and it has edge out from it
		visited.add(start)
		stack.append((0, [start]))

		while stack:
			dist, path = min(stack, key=lambda x: abs(distToGoal-x[0]))
			# find the path closest to the goal then extend the path

			node = path[-1]
			# to explore the outer node

			stack.remove((dist, path))
			# removes the nodes from stack
			
			visited.add(node)
			# add to the visited set

			if node in G.graph:

				for child, length in G.graph[node].items():
					if child not in visited:
						# if node not has been visited before and 
						# can be explored further

						if child==end:
							# halts, if found the end-node
							return path+[child]

						newDist = dist+length
						stack.append((newDist, path+[child]))
						# update the stack with new dist and path
						
	return f"Path does not exists between the Nodes ({start} to {end})"

if __name__ == "__main__":
	print(g4)
	print(' ')
	print(hillClimbing(g4, "s", "g", distToGoal=11))
