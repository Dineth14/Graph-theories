"""
floyd's algorithm to find shortest paths in a weighted graph with positive or negative edge weights (but with no negative cycles).

functions:
- floyd_warshall(graph): Implements Floyd's algorithm to find shortest paths.
- find_cycle(graph): Detects cycles in the graph using Floyd's algorithm.
- get_cycle_length(graph): Returns the length of the cycle if one exists.

"""

from typing import List, Dict, Tuple
import math

def floyd_warshall(graph: List[List[float]]) -> List[List[float]]:
    """Implements Floyd's algorithm to find shortest paths.

    Args:
        graph (List[List[float]]): Adjacency matrix representing the graph. Use float('inf') for no edge.

    Returns:
        List[List[float]]: Matrix of shortest path distances between all pairs of nodes.
    """
    num_nodes = len(graph)
    dist = [[math.inf] * num_nodes for _ in range(num_nodes)]

    for i in range(num_nodes):
        for j in range(num_nodes):
            dist[i][j] = graph[i][j]
        dist[i][i] = 0

    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def find_cycle(graph: Dict[int, List[int]]) -> bool:
    """Detects cycles in the graph using Floyd's algorithm.

    Args:
        graph (Dict[int, List[int]]): Adjacency list representing the graph.
    Returns:
        bool: True if a cycle is detected, False otherwise.
    """
    for start_node in graph:
        slow = start_node
        fast = start_node

        while True:
            if slow not in graph or fast not in graph or not graph[fast]:
                break
            slow = graph[slow][0]
            fast = graph[graph[fast][0]][0]

            if slow == fast:
                return True
    return False

def get_cycle_length(graph: Dict[int, List[int]]) -> int:
    """Returns the length of the cycle if one exists.

    Args:
        graph (Dict[int, List[int]]): Adjacency list representing the graph.

    Returns:
        int: Length of the cycle if detected, otherwise -1.
    """
    for start_node in graph:
        slow = start_node
        fast = start_node

        while True:
            if slow not in graph or fast not in graph or not graph[fast]:
                break
            slow = graph[slow][0]
            fast = graph[graph[fast][0]][0]

            if slow == fast:
                cycle_length = 1
                current = graph[slow][0]
                while current != slow:
                    cycle_length += 1
                    current = graph[current][0]
                return cycle_length
    return -1

# Example usage:
if __name__ == "__main__":
    graph = [
        [0, 3, math.inf, 7],
        [8, 0, 2, math.inf],
        [5, math.inf, 0, 1],
        [2, math.inf, math.inf, 0]
    ]

    shortest_paths = floyd_warshall(graph)
    print("Shortest path matrix using Floyd's Algorithm:")
    for row in shortest_paths:
        print(row)
