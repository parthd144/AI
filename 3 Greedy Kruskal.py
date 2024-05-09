class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(graph):
    # Initialize a list to store the edges of the minimum spanning tree
    mst_edges = []

    # Create a set to store all unique vertices in the graph
    vertices = set()
    for u, v, _ in graph:
        vertices.add(u)
        vertices.add(v)

    # Create a union-find data structure
    uf = UnionFind(vertices)

    # Sort the edges by weight in ascending order
    sorted_edges = sorted(graph, key=lambda x: x[2])

    # Iterate through the sorted edges and add the cheapest edge that does not form a cycle
    for edge in sorted_edges:
        u, v, weight = edge
        if uf.find(u) != uf.find(v):
            mst_edges.append(edge)
            uf.union(u, v)

    return mst_edges

# Example usage:
graph = [('A', 'B', 2), ('A', 'C', 4), ('B', 'C', 1), ('B', 'D', 9), ('C', 'D', 3)]
mst = kruskal(graph)
print("Minimum Spanning Tree edges : ")
for edge in mst:
    print(edge)
