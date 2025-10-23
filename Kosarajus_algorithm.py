"""
Kosaraju's Algorithm for Finding Strongly Connected Components (SCCs)
=====================================================================

A strongly connected component is a maximal set of vertices where every vertex
is reachable from every other vertex in the set.

Kosaraju's algorithm finds all SCCs in O(V + E) time using two DFS passes:
1. First DFS: Find finishing times (post-order)
2. Reverse the graph
3. Second DFS: Process vertices in decreasing finish time order

Time Complexity: O(V + E)
Space Complexity: O(V)

Functions:
- kosaraju_scc(graph: Dict[int, List[int]]) -> List[List[int]]:
    Finds all strongly connected components in a directed graph.
"""
from typing import Dict, List, Set


def kosaraju_scc(graph: Dict[int, List[int]]) -> List[List[int]]:
    """
    Implements Kosaraju's algorithm to find all strongly connected components.
    
    Algorithm Steps:
    1. Perform DFS on original graph to get finish times
    2. Reverse the graph edges
    3. Perform DFS on reversed graph in decreasing finish time order
    
    Args:
        graph: Adjacency list representing the directed graph
        
    Returns:
        List of SCCs, where each SCC is a list of node IDs
        
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    def dfs_first_pass(node: int, visited: Set[int], stack: List[int]) -> None:
        """First DFS to record finish times (post-order)."""
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_first_pass(neighbor, visited, stack)
        stack.append(node)  # Post-order: add after exploring all neighbors

    def dfs_second_pass(node: int, visited: Set[int], component: List[int], 
                       reversed_graph: Dict[int, List[int]]) -> None:
        """Second DFS to collect nodes in current SCC."""
        visited.add(node)
        component.append(node)
        for neighbor in reversed_graph.get(node, []):
            if neighbor not in visited:
                dfs_second_pass(neighbor, visited, component, reversed_graph)

    def reverse_graph(g: Dict[int, List[int]]) -> Dict[int, List[int]]:
        """Create a graph with all edges reversed."""
        reversed_g: Dict[int, List[int]] = {node: [] for node in g}
        for node in g:
            for neighbor in g[node]:
                if neighbor not in reversed_g:
                    reversed_g[neighbor] = []
                reversed_g[neighbor].append(node)
        return reversed_g

    # Step 1: First DFS to get finish times
    visited: Set[int] = set()
    finish_stack: List[int] = []
    
    for node in graph:
        if node not in visited:
            dfs_first_pass(node, visited, finish_stack)

    # Step 2: Reverse the graph
    reversed_graph = reverse_graph(graph)
    
    # Step 3: Second DFS in reverse finish order
    sccs: List[List[int]] = []
    visited.clear()

    while finish_stack:
        node = finish_stack.pop()  # Process in decreasing finish time
        if node not in visited:
            component: List[int] = []
            dfs_second_pass(node, visited, component, reversed_graph)
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
    