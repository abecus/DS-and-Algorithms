from graphExamples import *
from collections import deque
from collections import defaultdict


def bellmanFordSortestPath(start, end, graph):
    
    # initialising
    bestWeights = defaultdict(lambda: float('inf'))
    queue = deque()
    parentPointers = dict()
    bestWeights[start] = 0
    
    def bfs(start, graph, queue, bestWeights, parentPointers):
        childs = graph[start]   # getting childs of start       
        
        for child, weight in childs.items():
            """
            checking if node's child's weight is more than the
            weight of node to its and node's best weight do far
            """
            if  bestWeights[start] + weight < bestWeights[child]: 
                bestWeights[child] = bestWeights[start] + weight
                parentPointers[child] = start
                
                if child in queue:
                    continue
                else:
                    queue.appendleft(child)

        if not queue:
            """
            if queue is empty returning
            """
            return parentPointers, dict(bestWeights)
        
        return bfs(queue.pop(), graph, queue, bestWeights, parentPointers)   
             
    pointers, weigths = bfs(start, graph, queue, bestWeights, parentPointers)
    
    def prettiPath(pointer, graph, start, end):
        """
        returns a list with path from start to end with weights
        """
        temp = []
        while end!=start:
            temp.append(end)
            end = pointer[end]
        temp.append(end)
                
        path = []
        for i in reversed(range(1, len(temp))):
            path.append(f'[{ temp[i] }]---[ {graph[temp[i]][temp[i-1]]} ]--->')
        path.append(f"[{temp[0]}]")
        path = "".join(path)
        
        return path
            
    return prettiPath(pointers, graph, start, end)
        
if __name__ == "__main__":
    graph = negativeWeightDirectedGraph
    print(bellmanFordSortestPath("A", "B", graph))
    