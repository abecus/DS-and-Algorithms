import itertools


class Graph:
	def __init__(self, *args, **kwargs):
		self.graph = {}
		self.heuristicGraph = {}
		# self.Nodes = set()

	def _insertToGraph(self, fromNode, toNode=None, weight=None, heuristic=0):
		# self.Nodes.add(fromNode)
		# if toNode:
		# 	self.Nodes.add(toNode)

		if weight!=None:
			if (not heuristic) and fromNode not in self.graph:
				self.graph[fromNode] = {}

			elif heuristic and fromNode not in self.heuristicGraph:
				self.heuristicGraph[fromNode] = {}

			if toNode!=None:
				if heuristic:
					self.heuristicGraph[fromNode][toNode] = weight
				else:
					self.graph[fromNode][toNode] = weight
		
		else:
			if fromNode not in self.graph:
				self.graph[fromNode] = set()

			if toNode!=None:
				self.graph[fromNode].add(toNode)

	def add(self, fromNode, toNodes=None, weights=None, edgeType=0, heuristic=0):
		"""
		formNode:	a immutable object (str, int, etc)

		toNodes:	an iterable object

		weights:	an iterable object

		edgeType: {0: undirected, 1: directed}
		"""

		if weights!=None:
			assert len(toNodes)==len(weights), "numbers weights does not match to the numbers of edges"
			
			if edgeType:
				for node, weight in zip(toNodes, weights):
					if heuristic:
						self._insertToGraph(fromNode, node, weight, heuristic=1)
					else:
						self._insertToGraph(fromNode, node, weight)
						
			else:
				for node, weight in zip(toNodes, weights):
					if heuristic:
						self._insertToGraph(node, fromNode, weight, heuristic=1)
						self._insertToGraph(fromNode, node, weight, heuristic=1)
					else:
						self._insertToGraph(node, fromNode, weight)
						self._insertToGraph(fromNode, node, weight)

		elif toNodes!=None:
			if edgeType:
				for node in toNodes:
					self._insertToGraph(fromNode, node)
			else:
				for node in toNodes:
					self._insertToGraph(node, fromNode)
					self._insertToGraph(fromNode, node)
		else:
			self._insertToGraph(fromNode)

	def addFromDict(self, fromNode, nodesDict, edgeType=0):
		"""
		Used when, edges have weights to them

		formNode:	a immutable object (str, int, etc)

		nodesDict:	dict(node:weight)
		weight between node fromNode and node(the key)

		edgeType: {0: undirected, 1: directed}
		"""
		toNodes = [key for key in nodesDict.keys()]
		weights = [key for key in nodesDict.values()]
		self.add(fromNode, toNodes, weights, edgeType)

	def addHeuristicFromDict(self, fromNode, nodesDict, edgeType=0):
		"""
		Used when, edges have weights to them

		formNode:	a immutable object (str, int, etc)

		nodesDict:	dict(node:heuristic)
		weight between node fromNode and node(the key)

		edgeType: {0: undirected, 1: directed}
		"""
		toNodes = [key for key in nodesDict.keys()]
		heuristics = [key for key in nodesDict.values()]
		self.add(fromNode, toNodes, heuristics, edgeType=0, heuristic=1)

	def __str__(self):
		return "\n".join([f"{node}:{edge}" for node, edge in self.graph.items()])


	def getHeuristic(self, fromNode, toNode):
		"""
		returns the stored heuristic between the from-node to to-node
		if theirs nothing returns None
		"""
		return self.heuristicGraph.get(fromNode, {}).get(toNode, None)


	def getWeight(self, fromNode, toNode):
		"""
		returns the stored weight of edge between the from-node to to-node
		if theirs nothing returns None
		"""
		return self.graph.get(fromNode, {}).get(toNode, None)

	def getCost(self, path):
		"""
		returns the cost of traversing the path
  
		path: list (e.g. [start-node, n2, n3, ... end-node])
		"""
		cost = 0
		start = path[0]
		for n in itertools.islice(path, 1, len(path)):
			cost+=self.getWeight(start, n)
			start=n
		return cost
  
if __name__ == "__main__":
	# g1 = Graph()

	# g1.add(12, edgeType=0)

	# g1.add(4, [0], edgeType=1)
	# g1.add(8, [14, 4], edgeType=1)
	# g1.add(14, [13,0], edgeType=1)
	# g1.add(13, [0], edgeType=1)
	# g1.add(0, [8], edgeType=1)
 
	# g1.add(7, [6,11], edgeType=0)
	# g1.add(6, [7,11], edgeType=0)
	# g1.add(11, [7,6], edgeType=0)

	# g1.add(5, [17,16], edgeType=1)
	# g1.add(1, [5], edgeType=1)

	# g1.add(3,[9], edgeType=0)
	# g1.add(9,[15, 2], edgeType=0)
	# g1.add(2,[15], edgeType=0)
	# g1.add(15,[10], edgeType=0)

	# print(g1.graph)
 
# ___________________________________________________
 
	# g2 = Graph()
	# g2.add("a", ["b", "c"], [1, 4])
	# g2.add("b", ["d", "c"], [5, 1])
	# g2.add("c", ["d", "b"], [3, 1])
	# g2.add("d", ["e", "g", "f"], [8, 9, 3])
	# g2.add("e", ["g"], [2])
	# g2.add("f", ["g"], [5])
	# print(g2.graph)
	
	# ________________________same g2 graph as g3
	# g3  = Graph()
	# g3.addFromDict("a", {"b":1,"c":4})
	# g3.addFromDict("b", {"d":5,"c":1})
	# g3.addFromDict("c", {"d":3,"b":1})
	# g3.addFromDict("d", {"e":8,"g":9, "f":3})
	# g3.addFromDict("e", {"g":2})
	# g3.addFromDict("f", {"g":5})
	# print(g3.graph)

# ____________________________________________________
	g5 = Graph()
	g5.addFromDict("s", {"a":3,"b":5}, edgeType=1)
	g5.addFromDict("a", {"d":3,"b":4}, edgeType=1)
	g5.addFromDict("b", {"c":4}, edgeType=1)
	g5.addFromDict("d", {"g":5}, edgeType=1)
	g5.addFromDict("c", {"e":6}, edgeType=1)
	print(g5)
	
	g5.addHeuristicFromDict("s", {"g": 10.5})
	g5.addHeuristicFromDict("a", {"g": 7.5})
	g5.addHeuristicFromDict("b", {"g": 6})
	g5.addHeuristicFromDict("c", {"g": 7.5})
	g5.addHeuristicFromDict("g", {"g": 0})
	g5.addHeuristicFromDict("e", {"g": 5})
	g5.addHeuristicFromDict("d", {"g": 5})
	
	for key, val in g5.heuristicGraph.items():
		print(key, val)
   
	# print(g5.getWeight("s", "g"))
