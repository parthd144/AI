def greedy_shortest_path(graph, source):
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0  
    visited = set()

    while len(visited) < len(graph):
        min_distance_vertex = min((vertex, distance) for vertex, distance in distances.items() if vertex not in visited)[0]

        visited.add(min_distance_vertex)

        for neighbor, weight in graph[min_distance_vertex]:
            if neighbor not in visited:
                distances[neighbor] = min(distances[neighbor], distances[min_distance_vertex] + weight)

    return distances

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1), ('D', 7)],
    'C': [('D', 3)],
    'D': []
}
source_vertex = 'A'

shortest_distances = greedy_shortest_path(graph, source_vertex)
print("Shortest distances from the source vertex:")
for vertex, distance in shortest_distances.items():
    print(f"Distance from {source_vertex} to {vertex}: {distance}")
