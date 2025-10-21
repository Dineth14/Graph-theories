"""
2-SAT problem solver using implication graphs and Kosaraju's algorithm.

functions:
- two_sat_solver(clauses: List[Tuple[int, int]], num_vars: int) -> bool
- implication_graph(clauses: List[Tuple[int, int]], num_vars: int) -> Dict[int, List[int]]
- kosaraju_scc(graph: Dict[int, List[int]]) -> List[List[int]]

two_sat_solver: Determine if a given 2-SAT instance is satisfiable.
implication_graph: Construct the implication graph from 2-SAT clauses.
kosaraju_scc: Find strongly connected components in the implication graph.
"""

from typing import List, Tuple, Dict
from collections import defaultdict

def implication_graph(clauses: List[Tuple[int, int]], num_vars: int) -> Dict[int, List[int]]:
    """Construct the implication graph from 2-SAT clauses.

    Args:
        clauses (List[Tuple[int, int]]): List of clauses, each clause is a tuple of two literals.
        num_vars (int): Number of variables in the 2-SAT instance.

    Returns:
        Dict[int, List[int]]: Adjacency list representing the implication graph.
    """
    graph = defaultdict(list)

    for a, b in clauses:
        graph[-a].append(b)
        graph[-b].append(a)

    return graph

def two_sat_solver(clauses: List[Tuple[int, int]], num_vars: int) -> bool:
    """Determine if a given 2-SAT instance is satisfiable.

    Args:
        clauses (List[Tuple[int, int]]): List of clauses, each clause is a tuple of two literals.
        num_vars (int): Number of variables in the 2-SAT instance.

    Returns:
        bool: True if the 2-SAT instance is satisfiable, False otherwise.
    """
    graph = implication_graph(clauses, num_vars)
    sccs = kosaraju_scc(graph)

    component_id = {}
    for idx, component in enumerate(sccs):
        for node in component:
            component_id[node] = idx

    for var in range(1, num_vars + 1):
        if component_id.get(var, -1) == component_id.get(-var, -1):
            return False

    return True

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
    clauses = [
        (1, 2),
        (-1, 3),
        (-2, -3),
        (2, -3)
    ]
    num_vars = 3
    print("Is the 2-SAT instance satisfiable?", two_sat_solver(clauses, num_vars))  
    # Output: Is the 2-SAT instance satisfiable? True