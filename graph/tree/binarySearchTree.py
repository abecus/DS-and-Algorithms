#%%
class Node():

	def __init__(self, value, left=None, right=None):
	  self.value = value
	  self.left = left
	  self.right = right
	  
	def get(self):
		return self.value
		   
	def __getHeight(self):
		
		if self.left and self.right:
			return 1 + max(self.left.getHeight(), self.right.getHeight())
		
		elif self.left:
			return 1 + self.left.getHeight()
		
		elif self.right:
			return 1 + self.right.getHeight()

		else:
			return 1
		
	def __getSize(self):
		# gives number of nodes in tree
		if self.left and self.right:
			return 1 + self.left.getSize() + self.right.getSize()

		elif self.left:
			return 1 + self.left.getSize()

		elif self.right:
			return 1 + self.right.getSize()

		else:
			return 1
		
	def __repr__(self):
		return str(self.value)


class BST():

	def __init__(self):
		"""
		type heap: a list for a binary tree
		"""
		self.root = None
		
	def insert(self, value):
		if not self.root:
			self.root = Node(value)
			
		else:
			node = Node(value)
			self.__insertInTree(self.root, node)
		
	def __insertInTree(self, currentNode, node):
		if node.value < currentNode.value:
			if currentNode.left:
				return self.__insertInTree(currentNode.left, node)
			currentNode.left = node
				
		elif node.value > currentNode.value:
			if currentNode.right:
				return self.__insertInTree(currentNode.right, node)
			currentNode.right = node
				
	def find(self, value):
		return self.__findNode(self.root, value)
			
	def __findNode(self, currentNode, value):
		if currentNode == None:	
			return False

		if currentNode.value == value:
			return currentNode

		elif value < currentNode.value:
			return self.__findNode(currentNode.left, value)

		else:
			return self.__findNode(currentNode.right, value)
						   
	def getMax(self, node=None):
		"returns right most node of tree"
		curr_node = node if node else self.root
		if self.root:
			while curr_node.right:
				curr_node = curr_node.right
		return curr_node
	
	def getMin(self, node=None):
		"returns left most node of tree"
		curr_node = node if node else self.root
		if self.root:
			while curr_node.left:
				curr_node = curr_node.left
		return curr_node
				
	def getHeight(self):
		return Node.__getHeight(self.root)
	
	def getSize(self):
		return Node.__getSize(self.root)
	
	def preOrder(self, *, node=None):
		"returns iterator of tree nodes"
		curr_node = node if node else self.root

		def helper(curr_node):
			if curr_node==None:		return
			yield curr_node
			yield from helper(curr_node.left)
			yield from helper(curr_node.right)
				
		return helper(curr_node)
	
	def postOrder(self, *, node=None):
		"returns iterator of tree nodes"
		curr_node = node if node else self.root

		def helper(curr_node):
			if curr_node==None:		return
			yield from helper(curr_node.left)
			yield from helper(curr_node.right)
			yield curr_node
				
		return helper(curr_node)
	
	def inOrder(self, *, node=None):
		"returns iterator of tree nodes"
		curr_node = node if node else self.root

		def helper(curr_node):
			if curr_node==None:		return
			yield from helper(curr_node.left)
			yield curr_node
			yield from helper(curr_node.right)
				
		return helper(curr_node)
	
	def levelOrder(self, *, node=None):
		"returns iterator of List[tree nodes]"
		curr_node = node if node else self.root
		nodeList = [curr_node]
		yield nodeList.copy()

		while nodeList:
			temp = []
			for n in nodeList:
				if n.left:	temp.append(n.left)
				if n.right:	temp.append(n.right)
			
			yield temp.copy()
			nodeList = temp.copy()

	def delete(self, value):
		self.root = self.__del(self.root, value)
		
	@staticmethod
	def getRightMostVal(node):
		if not node.right:
			return node.value
		return BST.getRightMostVal(node.right)
	
	@staticmethod
	def removeRightMostAndGetLeftNode(node):
		if not node.right:
			return node.left
		node.right = BST.removeRightMostAndGetLeftNode(node.right)
		return node

	@staticmethod
	def __del(t, x):
		if t==None:
			return None
			
		if x > t.value:   
			t.right = BST.__del(t.right, x)
			
		elif x<t.value:   
			t.left = BST.__del(t.left, x)
			
		elif x == t.value:
			if t.left:
				t.value = BST.getRightMostVal(t.left)
				t.left = BST.removeRightMostAndGetLeftNode(t.left)
			else:
				t = t.right

		return t


#%%         
if __name__ == "__main__":
	import random
	# l = [-3, 6]
	l = [1, 5,-1, 6, 8, 0, 5]
	# l = [random.randint(0,1000) for _ in range(20)]
	bst = BST()

	for i in l:
		bst.insert(i)

	print([*map(lambda x: x.value, bst.inOrder(node=bst.root))])

	bst.delete(5)
	# bst.delete(6)
	# bst.delete(0)
	# bst.delete(8)
	# bst.delete(-1)
	# bst.delete(1)

	# print(bst.root.value)
	# print(bst.find(3), bst.find(7), bst.find(5))
	
	# print(bst.getHeight(bst.root))
	# print([*map(lambda x: x.value, bst.postOrder(node=bst.root))])
	# print([*map(lambda x: x.value, bst.inOrder(node=bst.root))])
	# print([*map(lambda x: x.value, bst.preOrder(node=bst.root))])
	# print([*map(lambda x: x.value, bst.levelOrder(node=bst.root))])
	
	
			 
		
	


#%%

