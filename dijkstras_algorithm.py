"""
Dijkstra's Algorithm for Shortest Paths (Non-Negative Weights Only)

"""

import heapq
from typing import Dict, List, Tuple, Set


def dijkstra(graph: Dict[int, List[Tuple[int, float]]], start_node: int) -> Dict[int, float]:
    """
    Perform Dijkstra's algorithm to find shortest paths from start_node.

    """
    if start_node not in graph:
        raise KeyError(f"Start node {start_node} not in graph")
    
    # Collect all vertices
    vertices: Set[int] = set(graph.keys())
    for neighbors in graph.values():
        for neighbor, weight in neighbors:
            if weight < 0:
                raise ValueError(
                    f"Dijkstra's algorithm cannot handle negative weights. "
                    f"Found edge with weight {weight}. Use Bellman-Ford instead."
                )
            vertices.add(neighbor)
    
    # Initialize distances
    distances: Dict[int, float] = {v: float('inf') for v in vertices}
    distances[start_node] = 0.0
    
    # Priority queue: (distance, vertex)
    pq: List[Tuple[float, int]] = [(0.0, start_node)]
    visited: Set[int] = set()
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        # Skip if already processed
        if u in visited:
            continue
        
        visited.add(u)
        
        # Skip if this is an outdated entry
        if current_dist > distances[u]:
            continue
        
        # Relax all edges from u
        for v, weight in graph.get(u, []):
            new_distance = distances[u] + weight
            
            if new_distance < distances[v]:
                distances[v] = new_distance
                heapq.heappush(pq, (new_distance, v))
    
    return distances


def dijkstra_with_path(graph: Dict[int, List[Tuple[int, float]]], 
                       start_node: int, 
                       end_node: int) -> Tuple[float, List[int]]:

    if start_node not in graph:
        raise KeyError(f"Start node {start_node} not in graph")
    
    # Collect all vertices and validate weights
    vertices: Set[int] = set(graph.keys())
    for neighbors in graph.values():
        for neighbor, weight in neighbors:
            if weight < 0:
                raise ValueError("Dijkstra's algorithm requires non-negative weights")
            vertices.add(neighbor)
    
    if end_node not in vertices:
        return (float('inf'), [])
    
    # Initialize
    distances: Dict[int, float] = {v: float('inf') for v in vertices}
    distances[start_node] = 0.0
    predecessors: Dict[int, int] = {}
    
    pq: List[Tuple[float, int]] = [(0.0, start_node)]
    visited: Set[int] = set()
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if u == end_node:
            break  # Early termination when target is reached
        
        if u in visited:
            continue
        
        visited.add(u)
        
        if current_dist > distances[u]:
            continue
        
        for v, weight in graph.get(u, []):
            new_distance = distances[u] + weight
            
            if new_distance < distances[v]:
                distances[v] = new_distance
                predecessors[v] = u
                heapq.heappush(pq, (new_distance, v))
    
    # Reconstruct path
    if distances[end_node] == float('inf'):
        return (float('inf'), [])
    
    path: List[int] = []
    current = end_node
    while current != start_node:
        path.append(current)
        if current not in predecessors:
            return (float('inf'), [])
        current = predecessors[current]
    path.append(start_node)
    path.reverse()
    
    return (distances[end_node], path)


# Example usage
if __name__ == "__main__":
    print("Dijkstra's Algorithm Demo")
    print("=" * 60)
    
    # Example 1: Simple graph
    print("\nExample 1: Simple shortest path")
    graph1: Dict[int, List[Tuple[int, float]]] = {
        0: [(1, 4.0), (2, 1.0)],
        1: [(3, 1.0)],
        2: [(1, 2.0), (3, 5.0)],
        3: []
    }
    
    print("Graph edges:")
    for u, edges in graph1.items():
        for v, w in edges:
            print(f"  {u} -> {v} (weight: {w})")
    
    distances = dijkstra(graph1, 0)
    print(f"\nShortest distances from node 0:")
    for node in sorted(distances.keys()):
        print(f"  To node {node}: {distances[node]}")
    
    # Show path to specific node
    dist, path = dijkstra_with_path(graph1, 0, 3)
    print(f"\nShortest path from 0 to 3: {path} (distance: {dist})")
    
    # Example 2: Larger graph
    print("\n" + "=" * 60)
    print("Example 2: Road network")
    road_network: Dict[int, List[Tuple[int, float]]] = {
        0: [(1, 7.0), (2, 9.0), (5, 14.0)],
        1: [(0, 7.0), (2, 10.0), (3, 15.0)],
        2: [(0, 9.0), (1, 10.0), (3, 11.0), (5, 2.0)],
        3: [(1, 15.0), (2, 11.0), (4, 6.0)],
        4: [(3, 6.0), (5, 9.0)],
        5: [(0, 14.0), (2, 2.0), (4, 9.0)]
    }
    
    print("Finding shortest paths from node 0:")
    distances2 = dijkstra(road_network, 0)
    for node in sorted(distances2.keys()):
        dist, path = dijkstra_with_path(road_network, 0, node)
        print(f"  To node {node}: distance={dist}, path={path}")
    
    # Example 3: Demonstrate negative weight detection
    print("\n" + "=" * 60)
    print("Example 3: Negative weight detection")
    negative_graph: Dict[int, List[Tuple[int, float]]] = {
        0: [(1, 5.0), (2, -3.0)],  # Negative weight!
        1: [(2, 2.0)],
        2: []
    }
    
    try:
        distances3 = dijkstra(negative_graph, 0)
    except ValueError as e:
        print(f"✓ Correctly detected: {e}")
        print("  Use Bellman-Ford algorithm for graphs with negative weights.")
