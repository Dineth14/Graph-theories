"""
 The Bellman–Ford algorithm1 finds shortest paths from a starting node to all
 nodes of the graph. The algorithm can process all kinds of graphs, provided that
 the graph does not contain a cycle with negative length. If the graph contains a
 negative cycle, the algorithm can detect this.
 The algorithm keeps track of distances from the starting node to all nodes
 of the graph. Initially, the distance to the starting node is 0 and the distance to
 all other nodes is infinite. The algorithm reduces the distances by finding edges
 that shorten the paths until it is not possible to reduce any distance.
"""

from typing import Dict, List, Tuple
def bellman_ford(graph: Dict[int, List[Tuple[int, float]]], start_node: int) -> Dict[int, float]:
    """Perform the Bellman-Ford algorithm to find shortest paths from start_node.
    
    param graph: Dict[int, List[Tuple[int, float]]]: The adjacency list of the graph with edge weights.
    param start_node: int: The node from which to start the shortest path calculations.
    Returns a dictionary with the shortest distance to each node from start_node.
    Raises a ValueError if a negative weight cycle is detected.
    """
    # Initialize distances from start_node to all other nodes as infinite
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0.0

    # Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    # Check for negative weight cycles
    for u in graph:
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative weight cycle")

    return distances

# Example usage
if __name__ == "__main__":
    # Defining a sample graph using an adjacency list with weights
    sample_graph = {
        0: [(1, 5), (2, 4)],
        1: [(3, 3), (4, 2)],
        2: [(1, 6)],
        3: [(4, -2)],
        4: [(5, 1)],
        5: [(3, -1)]
    }

    start_node = int(input("Enter the start node for Bellman-Ford: "))

    try:
        shortest_paths = bellman_ford(sample_graph, start_node=start_node)
        print(f"Shortest paths from node {start_node}: {shortest_paths}")
    except ValueError as e:
        print(e)