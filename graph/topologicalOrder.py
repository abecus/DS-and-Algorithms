from graphExamples import projectsGraph
from collections import OrderedDict

def topologicalSort(graph):
    visited = OrderedDict()

    def dfs(node):
        if not visited.get(i, 0):
            for adjnode in graph[node]:
                dfs(adjnode)
                visited[adjnode] = 1

    for i in graph.keys():
        dfs(i)

    visited.update({key:1 for key in graph.keys()})
    return list(visited.keys())

if __name__ == "__main__":
    print(topologicalSort(projectsGraph))
            
        