from graphExamples import *
from collections import defaultdict
import graph



class SetStack:
	"A stack with set to check if a object (non-mutable) in the stack"
	def __init__(self):
		self.stack, self.set = [], set()

	def pop(self)->None:
		ele = self.stack.pop()
		self.set.remove(ele)
		return ele

	def append(self, ele: object)->None:
		if ele not in self.set:
			self.stack.append(ele)
			self.set.add(ele)

	def doesContains(self, ele: object)->bool:
		return ele in self.set

	def __len__(self)->int:
		return len(self.stack)


def scc(G)-> (dict, int):
	# works on directed graph

	def dfs(root, i, stackSet, count):
		stackSet.append(root)	# put node on the stack

		# give node a new id and low-link value same as id
		idMap[root]=llValMap[root]=i
		i+=1

		# loop through all the adjcent-nodes of root and if its not been
		# visited do dfs no that node and on call-back if the adjcent-node
		# in the stack put the roots low-link value equal min of itself and
		# adjcent node's low-link value
		for node, _ in G.getAdjcentNodes(root):
			if idMap[node]==0:
				i, count = dfs(node, i, stackSet, count)
			if stackSet.doesContains(node):
				llValMap[root]=min(llValMap[node], llValMap[root])

		# if root node's id is equal to its low link value then its a start
		# of a strongly connected component, now pop off all the nodes from
		# stack and update the low link value of nodes to start of scc node's 
		# low link value
		if idMap[root]==llValMap[root]:
			node = stackSet.pop()
			while node!=root:
				llValMap[node] = idMap[root]
				node = stackSet.pop()
			count+=1
		return i, count


	count=0	# counts the scc
	idMap = defaultdict(lambda: 0)	# stores id of nodes
	stackSet = SetStack()	# stack with O(1) for checking if element in stack
	llValMap = {}	# stores low-link values of nodes
	i=1
 
	# loop through al the nodes and do dfs no them if 
	# they have not been visited before
	for node in G.nodes:
		if idMap[node]==0:
			i, count = dfs(node, i, stackSet, count)

	return llValMap, count


if __name__ == "__main__":
	G = g12
	# G = g13
	# print(G)
	print(scc(G))