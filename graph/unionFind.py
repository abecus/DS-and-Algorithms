from collections import defaultdict

class UnionFind:
	def __init__(self):
		self.parentsMap = {}	# tracks the parents of nodes
		self.rootLen = defaultdict(lambda:1)	# tracks no. of nodes in it
	
	def find(self, node: object)-> object:
		"returns the root node to the given (arg) node"
		# 1. creates parent-node of node if node not in parentsMap
		# 2. loops through the parents of given node till the root 
		# (the parent of given node is itself) not found and updates 
		# the parent of the nodes and returns the root of node.
		if node not in self.parentsMap:	self.parentsMap[node]=node
		while node!=self.parentsMap[node]:
			temp = self.parentsMap[node]
			self.parentsMap[node] = self.parentsMap[temp]
			node=temp
		return self.parentsMap[node]

	def union(self, node1: object, node2: object)-> None:
		# finds the roots of the given nodes and points a lower len root 
		# to other root
		parent1 = self.find(node1)
		parent2 = self.find(node2)
		if parent1!=parent2:
			if self.rootLen[parent1]<self.rootLen[parent2]:
				self.parentsMap[parent1]=parent2
				self.rootLen[parent2]+=self.rootLen[parent1]
			else:
				self.parentsMap[parent2]=parent1
				self.rootLen[parent1]+=self.rootLen[parent2]

	def isConnected(self, node1: object, node2: object)-> bool:
		# checks if roots of the given nodes are same and return true if 
		# they are else false
		return self.find(node1)==self.find(node2)

if __name__ == "__main__":
	n = 10
	edges = [(0, 1), (1, 2), (0, 9), (5, 6), (6, 4), (5, 9)]

	u = UnionFind()
	for i, j in edges:
		u.union(i, j)

	for i in range(n):
		print('item', i, '-> component', u.find(i))
