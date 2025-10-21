"""
Kosaraju's algorithm for finding strongly connected components (SCCs) in a directed graph.

functions:
- kosaraju_scc(graph: Dict[int, List[int]]) -> List[List[int]]:
    Implements Kosaraju's algorithm to find all strongly connected components in the graph.

    Args:
        graph (Dict[int, List[int]]): Adjacency list representing the graph.

    Returns:
        List[List[int]]: A list of strongly connected components, where each component is represented as a list of nodes.
"""
from git import List
from typing import Dict, List


def kosaraju_scc(graph: Dict[int, List[int]]) -> List[List[int]]:
    """Implements Kosaraju's algorithm to find all strongly connected components in the graph.

    Args:
        graph (Dict[int, List[int]]): Adjacency list representing the graph.

    Returns:
        List[List[int]]: A list of strongly connected components, where each component is represented as a list of nodes.
    """
    def dfs(node: int, visited: set, stack: List[int]):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, visited, stack)
        stack.append(node)

    def reverse_graph(graph: Dict[int, List[int]]) -> Dict[int, List[int]]:
        reversed_graph = {}
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                reversed_graph.setdefault(neighbor, []).append(node)
        return reversed_graph

    visited = set()
    stack = []
    for node in graph:
        if node not in visited:
            dfs(node, visited, stack)

    reversed_graph = reverse_graph(graph)
    sccs = []
    visited.clear()

    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs(node, visited, component)
            sccs.append(component)

    return sccs     

# Example usage:
if __name__ == "__main__":
    sample_graph = {
        0: [1],
        1: [2],
        2: [0, 3],
        3: [4],
        4: [5],
        5: [3],
        6: [5, 7],
        7: [6, 8],
        8: [9],
        9: [7]
    }

    sccs = kosaraju_scc(sample_graph)
    print("Strongly Connected Components:", sccs)
    