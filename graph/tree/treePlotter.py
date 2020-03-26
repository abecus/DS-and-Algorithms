from binarySearchTree import BST
from itertools import groupby
from collections import namedtuple
import heap

maxHeight = 1
lastRowLen = 0
nNodes = 0

def _initAtters(t):
	toString = str

	def dfs(root=t.root, height=1):
		global maxHeight, lastRowLen, nNodes
		if root!=None:
			lastRowLen += len(toString(root.value))
			nNodes+=1
			if root.left!=None:
				dfs(root.left, height+1)
			if root.right!=None:
				dfs(root.right, height+1)
			maxHeight = max(height, maxHeight)
	dfs()

def _getNodes(t, gap):
	_initAtters(t)
	at = 1<<maxHeight
	midPoint = at
	
	levels = []
	node = namedtuple("node", ["value", "level", "side", "at", "spread"])
 
	def dfs(root=t.root, level=1, side=2, at=at):
		if root!=None:
			spread = midPoint>>level
			levels.append(node(str(root.value), level, side, at+gap, spread))
			if root.left!=None:		dfs(root.left, level+1, 0, at-spread)
			if root.right!=None:	dfs(root.right, level+1, 1, at+spread)
	dfs()
	return levels

# puts _s, to both sides of the nodes
def render_(s, node, eachGap):
	s[node.at+eachGap] = node.value
	for i in range(node.at+eachGap-node.spread, node.at+eachGap):	s[i] = "_"		# left _s
	for i in range(node.at+eachGap+1, node.at+eachGap+node.spread+1):	s[i] = "_"	# right _s

# main function
def plot(tree, leftMargin=0):
	levels = _getNodes(tree, leftMargin)
	levels.sort(key=lambda x: (x.level, -x.at))	
	eachGap = lastRowLen//nNodes

	for level, nodes in groupby(levels, key=lambda x: x.level):
		node = next(nodes)
		# print(node)
		s = [" "]* (node.at+eachGap+node.spread+1)

		if level==maxHeight:	s[node.at+eachGap] = node.value
		else: render_(s, node, eachGap)
		for node in nodes:
			# print(node)
			if level==maxHeight:	s[node.at+eachGap] = node.value
			else:	render_(s, node, eachGap)

		print("".join(s))


if __name__ == "__main__":
	import random
	t = BST()
	l = [random.randint(1, 100) for _ in range(10)]
	for ele in l:
		t.insert(ele)
	plot(t)
	