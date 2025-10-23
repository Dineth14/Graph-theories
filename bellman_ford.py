"""
Bellman-Ford Algorithm for Shortest Paths with Negative Weights
================================================================

The Bellman-Ford algorithm finds shortest paths from a source vertex to all other
vertices in a weighted graph. Unlike Dijkstra's algorithm, it can handle negative
edge weights and detect negative cycles.

Algorithm:
1. Initialize distances: source = 0, all others = infinity
2. Relax all edges V-1 times (where V = number of vertices)
3. Check for negative cycles by trying one more relaxation

Key Properties:
- Can handle negative edge weights
- Detects negative cycles
- Time Complexity: O(V × E)
- Space Complexity: O(V)

Why V-1 iterations?
In a graph with V vertices, any shortest path can have at most V-1 edges
(without cycles). Each iteration guarantees finding shortest paths with
one more edge.
"""

from typing import Dict, List, Tuple, Set


def bellman_ford(graph: Dict[int, List[Tuple[int, float]]], start_node: int) -> Dict[int, float]:
    """
    Perform Bellman-Ford algorithm to find shortest paths from start_node.
    
    Args:
        graph: Adjacency list with edge weights. Format: {node: [(neighbor, weight), ...]}
        start_node: The source vertex
        
    Returns:
        Dictionary mapping each vertex to its shortest distance from start_node
        
    Raises:
        ValueError: If the graph contains a negative weight cycle reachable from start_node
        KeyError: If start_node is not in the graph
        
    Time Complexity: O(V × E) where V = vertices, E = edges
    Space Complexity: O(V)
    
    Example:
        >>> graph = {0: [(1, 4)], 1: [(2, -2)], 2: []}
        >>> bellman_ford(graph, 0)
        {0: 0.0, 1: 4.0, 2: 2.0}
    """
    if start_node not in graph:
        raise KeyError(f"Start node {start_node} not in graph")
    
    # Collect all vertices (including those only appearing as neighbors)
    vertices: Set[int] = set(graph.keys())
    for neighbors in graph.values():
        for neighbor, _ in neighbors:
            vertices.add(neighbor)
    
    # Initialize distances
    distances: Dict[int, float] = {v: float('inf') for v in vertices}
    distances[start_node] = 0.0
    
    num_vertices = len(vertices)
    
    # Relax all edges V-1 times
    for iteration in range(num_vertices - 1):
        updated = False
        for u in graph:
            if distances[u] == float('inf'):
                continue  # Skip unreachable vertices
                
            for v, weight in graph[u]:
                new_distance = distances[u] + weight
                if new_distance < distances[v]:
                    distances[v] = new_distance
                    updated = True
        
        # Early termination if no updates in this iteration
        if not updated:
            break
    
    # Check for negative weight cycles
    for u in graph:
        if distances[u] == float('inf'):
            continue
            
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                raise ValueError(
                    f"Graph contains a negative weight cycle reachable from node {start_node}. "
                    f"Cycle involves edge ({u}, {v}) with weight {weight}"
                )
    
    return distances

# Example usage
if __name__ == "__main__":
    print("Bellman-Ford Algorithm Demo")
    print("=" * 60)
    
    # Example 1: Graph with negative weights but no negative cycle
    print("\nExample 1: Negative weights (no cycle)")
    sample_graph1: Dict[int, List[Tuple[int, float]]] = {
        0: [(1, 5.0), (2, 4.0)],
        1: [(3, 3.0), (4, 2.0)],
        2: [(1, 6.0)],
        3: [(4, -2.0)],  # Negative edge
        4: [(5, 1.0)],
        5: []
    }
    
    print("Graph edges:")
    for u, edges in sample_graph1.items():
        for v, w in edges:
            print(f"  {u} -> {v} (weight: {w})")
    
    try:
        distances = bellman_ford(sample_graph1, 0)
        print(f"\nShortest distances from node 0:")
        for node in sorted(distances.keys()):
            dist = distances[node]
            print(f"  To node {node}: {dist if dist != float('inf') else '∞'}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Example 2: Graph with negative cycle
    print("\n" + "=" * 60)
    print("Example 2: Negative cycle detection")
    sample_graph2: Dict[int, List[Tuple[int, float]]] = {
        0: [(1, 5.0)],
        1: [(2, 3.0)],
        2: [(3, -2.0)],
        3: [(1, -8.0)]  # Creates negative cycle: 1->2->3->1 (total: 3-2-8 = -7)
    }
    
    print("Graph edges:")
    for u, edges in sample_graph2.items():
        for v, w in edges:
            print(f"  {u} -> {v} (weight: {w})")
    
    print("\nCycle: 1 -> 2 -> 3 -> 1")
    print("Total weight: 3 + (-2) + (-8) = -7 (negative!)")
    
    try:
        distances = bellman_ford(sample_graph2, 0)
        print(f"\nShortest distances from node 0: {distances}")
    except ValueError as e:
        print(f"\n✓ Correctly detected: {e}")
    
    # Interactive mode
    print("\n" + "=" * 60)
    response = input("\nTry with custom start node? (y/n): ").strip().lower()
    if response == 'y':
        start_node = int(input("Enter start node for Example 1: "))
        try:
            shortest_paths = bellman_ford(sample_graph1, start_node)
            print(f"\nShortest paths from node {start_node}:")
            for node in sorted(shortest_paths.keys()):
                dist = shortest_paths[node]
                print(f"  To node {node}: {dist if dist != float('inf') else '∞'}")
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")