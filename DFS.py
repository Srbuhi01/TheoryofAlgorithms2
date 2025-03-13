graph = {
    0: [9],
    1: [0],
    2: [],
    3: [2, 4, 5],
    4: [],
    5: [6],
    6: [7],
    7: [3, 10],
    8: [1, 7],
    9: [8],
    10: [11],
    11: [7],
    12: []
}

visited = set()

def DFS(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(node)
        
        for neighbor in graph[node]:
            DFS(graph, neighbor, visited)

DFS(graph, 0 , visited)            
