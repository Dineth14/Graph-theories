"""
Primes algorithm to find minimum spanning trees
"""

from typing import List, Tuple
import heapq

def primes_algorithm(num_nodes: int, edges: List[Tuple[int, int, float]]) -> List[Tuple[int, int, float]]:
    """Find the minimum spanning tree using Prim's algorithm.

    Args:
        num_nodes (int): Number of nodes in the graph.
        edges (List[Tuple[int, int, float]]): List of edges in the form (u, v, weight).

    Returns:
        List[Tuple[int, int, float]]: Edges in the minimum spanning tree.
    """
    adjacency_list = {i: [] for i in range(num_nodes)}
    for u, v, weight in edges:
        adjacency_list[u].append((weight, v))
        adjacency_list[v].append((weight, u))

    mst_edges = []
    visited = [False] * num_nodes
    min_heap = [(0, 0, -1)]  # (weight, current_node, parent_node)

    while min_heap:
        weight, current_node, parent_node = heapq.heappop(min_heap)
        if visited[current_node]:
            continue
        visited[current_node] = True
        if parent_node != -1:
            mst_edges.append((parent_node, current_node, weight))

        for edge in adjacency_list[current_node]:
            if not visited[edge[1]]:
                heapq.heappush(min_heap, (edge[0], edge[1], current_node))

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

    mst = primes_algorithm(num_nodes, edges)
    print("Edges in the Minimum Spanning Tree using Prim's Algorithm:")
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")