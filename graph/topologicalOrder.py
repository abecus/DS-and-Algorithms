from graphExamples import *


def topologicalSort(G):
	"""
	itype: graph
	rtype: list
	"""
	# no check for cycles in the this algorithm
 
	visited = set()
	order = []

	def dfs(node):
		for adjNode, _ in G.getAdjcentNodes(node):
			# call dfs till the leaf node
			if adjNode not in visited:
				visited.add(adjNode)
				dfs(adjNode)

				# pop up the stack and add the popped nodes to
				# the visited set and append the node to the order list
				order.append(adjNode)

	for node in G.nodes:
		# loop through all the node available in the graph
		# if not have been visited
		if node not in visited:
			dfs(node)

	# extend the nodes which were not been able 
	# to explore to the end of the order list 
	return reversed(order+[node for node in G.nodes if node not in visited])

if __name__ == "__main__":
	# G = Graph()
	# G.add("a", ['d'], edgeType=1)
	# G.add("d", ['h', 'g'], edgeType=1)
	# G.add("h", ['j', 'i'], edgeType=1)
	# G.add("g", ['i'], edgeType=1)
	# G.add("i", ['l'], edgeType=1)
	# G.add("j", ['i', 'm'], edgeType=1)
	# G.add("j", ['i', 'm'], edgeType=1)
	# G.add("c", ['a', 'b'], edgeType=1)
	# G.add("b", ['d'], edgeType=1)
	# G.add("e", ['d', 'a', 'f'], edgeType=1)
	# G.add("f", ['j', 'k'], edgeType=1)
	# G.add("f", ['j', 'k'], edgeType=1)
	# G.add("k", ['j'], edgeType=1)
	# G.description = "A DAG"

	G=g6	# same graph as above
	# print(G.description)
	print(*topologicalSort(G))