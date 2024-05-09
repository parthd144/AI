def prim(graph, start):
    # Initialize sets to keep track of visited and unvisited vertices
    visited = set()
    visited.add(start)
    unvisited = set(graph.keys())
    unvisited.remove(start)
    
    # Initialize a list to store the edges of the minimum spanning tree
    mst_edges = []
    
    # Loop until all vertices are visited
    while unvisited:
        min_weight = float('inf')
        min_edge = None
        
        # Find the minimum weight edge that connects a vertex in the tree to a vertex outside the tree
        for u in visited:
            for v, weight in graph[u]:
                if v in unvisited and weight < min_weight:
                    min_weight = weight
                    min_edge = (u, v, weight)
        
        # Add the minimum weight edge to the minimum spanning tree
        mst_edges.append(min_edge)
        
        # Update visited and unvisited sets
        visited.add(min_edge[1])
        unvisited.remove(min_edge[1])
    
    return mst_edges

# Example usage:
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 9)],
    'C': [('A', 4), ('B', 1), ('D', 3)],
    'D': [('B', 9), ('C', 3)]
}
start_vertex = 'A'

mst = prim(graph, start_vertex)
print("Minimum Spanning Tree edges : ")
for edge in mst:
    print(edge)
