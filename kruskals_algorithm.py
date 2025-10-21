"""
Kruskal's algorithm for finding the minimum spanning tree of a connected, undirected graph.

functions:
- kruskals_algorithm(num_nodes: int, edges: List[Tuple[int, int, float]]) -> List[Tuple[int, int, float]]
kruskals_algorithm: Find the minimum spanning tree using Kruskal's algorithm.
"""

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

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

def kruskals_algorithm(num_nodes, edges):
    """Find the minimum spanning tree using Kruskal's algorithm.

    Args:
        num_nodes (int): Number of nodes in the graph.
        edges (List[Tuple[int, int, float]]): List of edges in the form (u, v, weight).

    Returns:
        List[Tuple[int, int, float]]: Edges in the minimum spanning tree.
    """
    # Sort edges based on their weights
    edges.sort(key=lambda x: x[2])
    
    disjoint_set = DisjointSet(num_nodes)
    mst_edges = []

    for u, v, weight in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst_edges.append((u, v, weight))

    return mst_edges

# Example usage:
if __name__ == "__main__":
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    num_nodes = 4
    mst = kruskals_algorithm(num_nodes, edges)
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")

