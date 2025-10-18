"""
The SPFA algorithm ("Shortest Path Faster Algorithm") is a variant of the
Bellman–Ford algorithm, that is often more efficient than the original algorithm.
The SPFA algorithm does not go through all the edges on each round, but instead,
it chooses the edges to be examined in a more intelligent way.
The algorithm maintains a queue of nodes that might be used for reducing
the distances. First, the algorithm adds the starting node x to the queue. Then,
the algorithm always processes the first node in the queue, and when traversing an edge
a→b results in a shorter distance to node b, node b is added to the queue.
The efficiency of the SPFA algorithm depends on the structure of the graph:
the algorithm is often efficient, but its worst case time complexity is still $O(nm)$,
where $n$ is the number of nodes and $m$ is the number of edges, and it is possible to create inputs that make the algorithm as slow as the original
Bellman–Ford algorithm.
"""
from collections import deque
from typing import Dict, List, Tuple    

def spfa(graph: Dict[int, List[Tuple[int, float]]], start_node: int) -> Dict[int, float]:
    """Perform the SPFA algorithm to find shortest paths from start_node.
    
    param graph: Dict[int, List[Tuple[int, float]]]: The adjacency list of the graph with edge weights.
    param start_node: int: The node from which to start the shortest path calculations.
    Returns a dictionary with the shortest distance to each node from start_node.
    Raises a ValueError if a negative weight cycle is detected.
    """
    # Collect all nodes (keys and any nodes that appear as edge targets)
    nodes = set(graph.keys())
    for u, edges in graph.items():
        for v, _ in edges:
            nodes.add(v)

    if start_node not in nodes:
        raise ValueError(f"start_node {start_node} is not present in graph")

    # Initialize distances from start_node to all other nodes as infinite
    distances = {node: float('inf') for node in nodes}
    distances[start_node] = 0.0

    # Queue for processing nodes
    queue = deque([start_node])
    in_queue = {node: False for node in nodes}
    in_queue[start_node] = True

    # Count relaxations per node to detect negative-weight cycles
    relax_count = {node: 0 for node in nodes}
    max_relax = max(0, len(nodes) - 1)

    while queue:
        u = queue.popleft()
        in_queue[u] = False

        for v, weight in graph.get(u, []):
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                relax_count[v] += 1
                if relax_count[v] > max_relax:
                    # A vertex was relaxed more than n-1 times -> negative cycle
                    raise ValueError("Negative weight cycle detected")
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True

    return distances

# Example usage
if __name__ == "__main__":
    # Defining a sample graph using an adjacency list with weights
    sample_graph = {
        0: [(1, 5.0), (2, 4.0)],
        1: [(3, 3.0), (4, 2.0)],
        2: [(1, 6.0)],
        3: [(4, -2.0)],
        4: [(5, 1.0)],
        5: [(3, -1.0)]
    }

    start_node = int(input("Enter the start node for SPFA: "))

    try:
        shortest_paths = spfa(sample_graph, start_node=start_node)
        print(f"Shortest paths from node {start_node}: {shortest_paths}")
        print("SPFA traversal complete.")
    except ValueError as exc:
        print(f"SPFA error: {exc}")