"""
eularian path in a graph.
the eularian path is a trail in a graph that visits every edge exactly once.

functions:
- has_eularian_path(num_nodes: int, edges: List[Tuple[int, int]]) -> bool
- find_eularian_path(num_nodes: int, edges: List[Tuple[int, int]]) -> List[int]


has_eularian_path: Check if the graph has an eularian path.
find_eularian_path: Find the eularian path in the graph if it exists.
"""

from typing import List, Tuple, Dict
from collections import defaultdict, deque

def has_eularian_path(num_nodes: int, edges: List[Tuple[int, int]]) -> bool:
    """Check if the graph has an eularian path."""
    degree = [0] * num_nodes
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1

    odd_count = sum(1 for deg in degree if deg % 2 != 0)
    return odd_count == 0 or odd_count == 2

def find_eularian_path(num_nodes: int, edges: List[Tuple[int, int]]) -> List[int]:
    """Find the eularian path in the graph if it exists."""
    if not has_eularian_path(num_nodes, edges):
        return []

    graph = defaultdict(deque)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    start_node = 0
    for i in range(num_nodes):
        if len(graph[i]) % 2 != 0:
            start_node = i
            break

    path = []
    stack = [start_node]

    while stack:
        u = stack[-1]
        if graph[u]:
            v = graph[u].popleft()
            graph[v].remove(u)
            stack.append(v)
        else:
            path.append(stack.pop())

    return path[::-1]

# Example usage:
if __name__ == "__main__":
    edges = [
        (0, 1),
        (1, 2),
        (2, 0),
        (1, 3),
        (3, 4),
        (4, 1)
    ]
    num_nodes = 5

    if has_eularian_path(num_nodes, edges):
        path = find_eularian_path(num_nodes, edges)
        print("Eularian Path found:", path)
    else:
        print("No Eularian Path exists in the graph.")