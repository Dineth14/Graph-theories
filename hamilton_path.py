"""
hamiltonian path in a graph.
a hamiltonian path is a path in an undirected or directed graph that visits each vertex

functions:
- has_hamiltonian_path(num_nodes: int, edges: List[Tuple[int, int]]) -> bool
- find_hamiltonian_path(num_nodes: int, edges: List[Tuple[int, int]]) -> List[int]

"""

from typing import List, Tuple, Dict
from collections import defaultdict

def has_hamiltonian_path(num_nodes: int, edges: List[Tuple[int, int]]) -> bool:
    """Check if the graph has a hamiltonian path using backtracking."""
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def backtrack(path):
        if len(path) == num_nodes:
            return True
        last_node = path[-1]
        for neighbor in graph[last_node]:
            if neighbor not in path:
                path.append(neighbor)
                if backtrack(path):
                    return True
                path.pop()
        return False

    for start_node in range(num_nodes):
        if backtrack([start_node]):
            return True
    return False

def find_hamiltonian_path(num_nodes: int, edges: List[Tuple[int, int]]) -> List[int]:
    """Find the hamiltonian path in the graph if it exists."""
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def backtrack(path):
        if len(path) == num_nodes:
            return True
        last_node = path[-1]
        for neighbor in graph[last_node]:
            if neighbor not in path:
                path.append(neighbor)
                if backtrack(path):
                    return True
                path.pop()
        return False

    for start_node in range(num_nodes):
        path = [start_node]
        if backtrack(path):
            return path
    return []

# Example usage:
if __name__ == "__main__":
    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (1, 3)
    ]
    num_nodes = 4

    if has_hamiltonian_path(num_nodes, edges):
        path = find_hamiltonian_path(num_nodes, edges)
        print("Hamiltonian Path found:", path)
    else:
        print("No Hamiltonian Path exists.")