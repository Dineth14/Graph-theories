"""
Floyd-Warshall Algorithm Implementation
-----------------------------
This module implements the Floyd-Warshall algorithm to find the shortest paths
between all pairs of nodes in a weighted graph. The algorithm can handle graphs
with negative edge weights but no negative cycles.
"""

from typing import Dict, List, Tuple

# Floyd-Warshall Algorithm
def floyd_warshall(graph: Dict[int, List[Tuple[int, float]]]) -> Dict[Tuple[int, int], float]:
    """Perform the Floyd-Warshall algorithm to find shortest paths between all pairs of nodes.
    
    param graph: Dict[int, List[Tuple[int, float]]]: The adjacency list of the graph with edge weights.
    Returns a dictionary with the shortest distance between each pair of nodes.
    Raises a ValueError if a negative weight cycle is detected.
    """
    # Initialize distances with infinity
    nodes = list(graph.keys())
    distances = {(i, j): float('inf') for i in nodes for j in nodes}
    
    # Set distance to self as 0 and direct edges as their weights
    for node in nodes:
        distances[(node, node)] = 0.0
        for neighbor, weight in graph[node]:
            distances[(node, neighbor)] = weight

    # Floyd-Warshall algorithm
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if distances[(i, k)] + distances[(k, j)] < distances[(i, j)]:
                    distances[(i, j)] = distances[(i, k)] + distances[(k, j)]

    # Check for negative weight cycles
    for node in nodes:
        if distances[(node, node)] < 0:
            raise ValueError("Graph contains a negative weight cycle")

    return distances

# Example usage
if __name__ == "__main__":
    # Defining a sample graph using an adjacency list with weights
    sample_graph = {
        0: [(1, 3), (2, 8), (4, -4)],
        1: [(3, 1), (4, 7)],
        2: [(1, 4)],
        3: [(0, 2), (2, -5)],
        4: [(3, 6)]
    }

    try:
        shortest_paths = floyd_warshall(sample_graph)
        print("Shortest paths between all pairs of nodes:")
        for (i, j), dist in shortest_paths.items():
            print(f"Distance from node {i} to node {j}: {dist}")
    except ValueError as e:
        print(e)    

        