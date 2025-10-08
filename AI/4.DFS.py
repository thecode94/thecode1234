#implement depth-First search(DFS) in samll graph
graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[],
    }
def dfs(graph,start,visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)
#start dfs form node 'A'
print("DFS Traversal starting for Node A :")
dfs(graph,'A')