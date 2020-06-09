from collections import defaultdict
import heapq as heap
 
def dijkstra(G, startingNode):
	visited = set()
	pq = []
	nodeCosts = defaultdict(lambda: float('inf'))
	nodeCosts[startingNode] = 0
	heap.heappush(pq, (0, startingNode))
 
	# while priorityQueue:
	while pq:
		# go greedily by always extending the shorter cost nodes first
		_, node = heap.heappop(pq)
 
		visited.add(node)
 
		for adjNode, weight in G[node].items():
			if adjNode in visited:  continue
 
			newCost = nodeCosts[node]+weight
			if nodeCosts[adjNode] > newCost:
				nodeCosts[adjNode]=newCost
				heap.heappush(pq, (newCost, adjNode))
	return nodeCosts
# Write your code here
 
for _ in range(int(input())):
    n,m=[*map(int, input().split())]
    g=defaultdict(dict)
    for _ in range(m):
        s,e,c=[*map(int, input().split())]
        if e in g[s]:   g[s][e]=min(g[s][e], c)
        else:   g[s][e]=c

        if s in g[e]:   g[e][s]=min(g[e][s], c)
        else:   g[e][s]=c

    costs = dijkstra(g, 1)
    # print(g)
    # print(costs)
    for _ in range(int(input())):
        a,k=[*map(int, input().split())]
        travelCost=costs[a]*2
        res=0 if k-travelCost>=float("inf") else k-travelCost
        print(max(0, res))