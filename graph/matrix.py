from collections import defaultdict
import heapq as heap

# Complete the minTime function below.
def getArts(G,n,root):
	
	def dfs(root, at, parent):
		oEdge=0
		seen[at]=1
		for node in G.get(at, tuple()):
			if node==parent:    continue
			if not seen[node]:
				oEdge+=1
				dfs(root, node, at)
				low[at] = min(low[at], low[node])
				if (parent==-1 and oEdge>1) or (low[at]<=low[node] and parent!=-1):
					arts.add(at)
			else:
				low[at]=min(low[at], ids[parent])

	seen = [0]*n
	low = [*range(n)]
	ids = [*range(n)]
	arts = set()
	for root in range(n):
		if not seen[root] and root in G:
			dfs(root, root, -1)
	return arts

def minTime(roads, machines, n):
	graph = defaultdict(dict)
	nodes = set()
	for f,t,time in roads:graph[f][t]=time;graph[t][f]=time; nodes.add(f);nodes.add(t)
 
	def dfs(root, at, parent):
		oEdge=0
		seen[at]=1
		for node in graph.get(at, tuple()):
			if node==parent:	continue
			if not seen[node]:
				oEdge+=1
				dfs(root, node, at)
				low[at] = min(low[at], low[node])
				if (parent==-1 and oEdge>1) or (low[at]<=low[node] and parent!=-1):
					arts.add(at)
			else:	low[at]=min(low[at], ids[parent])

	mach = [0]*n
	for i in machines:	mach[i]=1
 
	res=0
	seen = [0]*n
	low = [*range(n)]
	ids = [*range(n)]
	for root in range(n):
		if not seen[root] and root in graph:
			arts = set()
			vals=set()
			dfs(root, root, -1)
			for i, ele in enumerate(iter(sorted(arts))):
				if i<n-1:	res+=graph[root][ele]
	return res
	
 
	
	# for node in arts:
	# 	h = []
		# for to in graph[node]:
		# 	if mach[to] and not removed[to]:
		# 		heap.heappush(h, graph[node][to])
		# 		removed[to]=1
		# while len(h)>1:
		# 	res+=heap.heappop(h)
	return res
# do it separately using connected components
if __name__ == "__main__":
	roads=[
		[0, 1, 4],
		[1, 2, 3],
		[1, 3, 7],
		[0, 4, 2]
		]
	machines=[2,3,4]
	n=5
	print(minTime(roads,machines,n))