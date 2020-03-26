from graph import Graph
from itertools import combinations, product, permutations


def tsp_bruteForce(G, start):
    # loop through all possible path and finds the optimal
    # tour/cycle with min cost
    N=len([*G.nodes])
    res=None
    cost=float('inf')
    for path in permutations(range(N)):
        s=path[0]
        if s!=start:    continue
        nCost=G.getPathCost(path)+G.getWeight(path[-1], s)
        if nCost<cost:
            res=path
            cost=nCost
    return cost, list(res)+[res[0]]

def tsp(G:Graph, start:"node"=0):
    # main function for tsp

    N=len([*G.nodes])
    # dp table (N x 2^N) keeps all states each row is for a node
    # and has 2^N columns representing a path as integer (1011-> 
    # path with node 0,2 and 3) 
    dp=[[float("inf")]*pow(2, N)]*N
    setup(G, dp, start, N)
    solve(G, dp, start, N)
    tour = findOptimalTour(G, dp, start, N)
    minCost = findMinCost(G, start, tour)
    return minCost, tour

def setup(G, dp, start, N):
    # use to all two node path are filled in the dp table
    for i in range(N):
        if i!=start:
            dp[i][(1<<start)|(1<<i)] = G.getWeight(start, i)
            
def solve(G, dp, start, N):
    # solves the tsp and fills the dp table for further use
    
    # loop through all paths with r nodes in it
    for r in range(3, N+1):
        # bin_combinations(3, 4) -> 1110, 1101, 1011, 0111
        for subset in bin_combinations(r, N):
            if notIn(start, subset):    continue
            # looking for all possible next nodes from path 
            # of r-2 nodes
            for next in range(N):
                if next==start or notIn(next, subset):  continue
                # removing next node from the path (subset)
                # and finding min cost over all (start->end->next) 
                # end nodes and filling that to dp table
                state=subset^(1<<next)
                minDist=float('inf')
                for end in range(N):
                    if end==start or end==next or notIn(end, subset):   continue
                    minDist= min(minDist, dp[end][state]+G.getWeight(end, next))
                dp[next][subset]=minDist

# checks if node is not in subset
notIn = lambda node, subset : (subset&(1<<node))==0

def bin_combinations(r, N):
    # generator for generating
    # as bin_combinations(3, 4) -> 1110, 1101, 1011, 0111
    for index in combinations(range(N), r):
        s=0
        for i in index:
            s|=(1<<i)
        yield s
    
def findMinCost(G, start, tour):
    # endState = (1<<N)-1
    # print(" ", *[*range(2**N)], sep="   ")
    # print(dp)
    # return min(dp[end][endState]+G.getWeight(end, start) 
    #            for end in range(N) if end!=start)
    
    # returns the cost of the tour
    return g.getPathCost(tour)
    
def findOptimalTour(G, dp, start, N):
    # creates tour/cycle from the dp table 
    # by backward travelling from end node to 
    # the start node
    
    lastIndex = start
    # end state str([1]*N)
    state = (1<<N)-1
    # list to keep the tour nodes
    tour = [None]*(N+1)
    
    # filling the tour list in reversed order
    for i in reversed(range(1,N)):
        index=-1
        # finds min over all nodes j from lastIndex node 
        # to it and updates the last index as that 
        # min index and updates the state by removing 
        # min index node from the state
        for j in range(N):
            if j==start or notIn(j, state):    continue
            if index==-1:   index=j
            prevDist=dp[index][state]+g.getWeight(index, lastIndex)
            newDist=dp[j][state]+g.getWeight(j, lastIndex)
            if prevDist>newDist:
                index=j
        tour[i]=index
        state=(state^(1<<index))
        lastIndex=index
        
    # first and last nodes in tour list as start node
    tour[0]=tour[-1]=start
    return tour
    
    
if __name__ == "__main__":
    # g = Graph()
    # g.addFromDict(0, {1:4, 2:1, 3:9, 4:100}, edgeType=1)
    # g.addFromDict(1, {0:3, 2:6, 3:11, 4:100}, edgeType=1)
    # g.addFromDict(2, {0:4, 1:1, 3:2, 4:100}, edgeType=1)
    # g.addFromDict(3, {0:6, 1:5, 2:-4, 4:100}, edgeType=1)
    # g.addFromDict(4, {0:6, 1:5, 2:-4, 3:-100}, edgeType=1)
    
    g=Graph()
    g.addFromDict(0, {1:10, 2:15, 3:20}, edgeType=1)
    g.addFromDict(1, {0:10, 2:35, 3:25}, edgeType=1)
    g.addFromDict(2, {0:15, 1:35, 3:30}, edgeType=1)
    g.addFromDict(3, {0:20, 1:25, 2:30}, edgeType=1)
    # [[0, 10, 15, 20], 
    #  [10, 0, 35, 25], 
    #  [15, 35, 0, 30], 
    #  [20, 25, 30, 0]
    #  ]
    
    s=2
    cost, tour = tsp(g, s)
    print(tour, cost)
    
    # cost, tour = tsp_bruteForce(g, s)
    # print(tour, cost)
    