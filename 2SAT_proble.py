"""
2-SAT Problem Solver Using Implication Graphs
==============================================

The 2-SAT (2-Satisfiability) problem asks: given a Boolean formula in
Conjunctive Normal Form (CNF) where each clause has exactly 2 literals,
is there an assignment of TRUE/FALSE to variables that satisfies all clauses?

Example:
    (x1 OR x2) AND (NOT x1 OR x3) AND (NOT x2 OR NOT x3) AND (x2 OR NOT x3)
    
Key Insight:
    Each clause (a OR b) can be written as implications:
    - NOT a => b  (if a is false, b must be true)
    - NOT b => a  (if b is false, a must be true)

Algorithm:
1. Build implication graph from clauses
2. Find strongly connected components (SCCs) using Kosaraju's algorithm
3. Check if any variable x and NOT x are in the same SCC
   - If yes: unsatisfiable (contradiction)
   - If no: satisfiable

Time Complexity: O(V + E) where V = 2n variables, E = 2m edges
Space Complexity: O(V + E)

Functions:
- implication_graph: Convert 2-SAT clauses to implication graph
- two_sat_solver: Check if 2-SAT instance is satisfiable
- kosaraju_scc: Find strongly connected components
"""

from typing import List, Tuple, Dict
from collections import defaultdict

def implication_graph(clauses: List[Tuple[int, int]], num_vars: int) -> Dict[int, List[int]]:
    """
    Construct the implication graph from 2-SAT clauses.
    
    Each clause (a OR b) creates two implications:
    - NOT a => b  (if a is false, b must be true)
    - NOT b => a  (if b is false, a must be true)
    
    Variable representation:
    - Positive literal x is represented as x
    - Negative literal NOT x is represented as -x

    Args:
        clauses: List of clauses, each clause is (literal1, literal2)
        num_vars: Number of Boolean variables (not used, kept for API consistency)

    Returns:
        Implication graph as adjacency list
        
    Example:
        clause (x1 OR x2) creates edges: -x1 -> x2 and -x2 -> x1
        clause (x1 OR NOT x2) creates edges: -x1 -> -x2 and x2 -> x1
    """
    graph: Dict[int, List[int]] = defaultdict(list)

    for a, b in clauses:
        # Clause (a OR b) => implications: NOT a => b and NOT b => a
        graph[-a].append(b)
        graph[-b].append(a)

    return dict(graph)

def two_sat_solver(clauses: List[Tuple[int, int]], num_vars: int) -> bool:
    """
    Determine if a 2-SAT instance is satisfiable.
    
    The key insight: A 2-SAT formula is unsatisfiable if and only if
    there exists a variable x such that x and NOT x are in the same
    strongly connected component (SCC).
    
    Why? If x and NOT x are in the same SCC, then:
    - x => NOT x (x being true implies x must be false)
    - NOT x => x (x being false implies x must be true)
    This is a contradiction!

    Args:
        clauses: List of clauses, each clause is (literal1, literal2)
        num_vars: Number of Boolean variables

    Returns:
        True if satisfiable, False otherwise
        
    Time Complexity: O(n + m) where n = variables, m = clauses
    """
    # Build implication graph
    graph = implication_graph(clauses, num_vars)
    
    # Find strongly connected components
    sccs = kosaraju_scc(graph)

    # Map each literal to its SCC ID
    component_id: Dict[int, int] = {}
    for idx, component in enumerate(sccs):
        for node in component:
            component_id[node] = idx

    # Check for contradictions
    for var in range(1, num_vars + 1):
        # If variable and its negation are in same SCC => unsatisfiable
        var_comp = component_id.get(var, -1)
        neg_var_comp = component_id.get(-var, -1)
        
        if var_comp != -1 and var_comp == neg_var_comp:
            return False

    return True

def kosaraju_scc(graph: Dict[int, List[int]]) -> List[List[int]]:
    """
    Find strongly connected components using Kosaraju's algorithm.
    
    Args:
        graph: Adjacency list representing the directed graph
        
    Returns:
        List of SCCs, where each SCC is a list of node IDs
        
    Time Complexity: O(V + E)
    """
    from typing import Set
    
    def dfs_first(node: int, visited: Set[int], stack: List[int]) -> None:
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_first(neighbor, visited, stack)
        stack.append(node)

    def dfs_second(node: int, visited: Set[int], component: List[int], 
                   rev_graph: Dict[int, List[int]]) -> None:
        visited.add(node)
        component.append(node)
        for neighbor in rev_graph.get(node, []):
            if neighbor not in visited:
                dfs_second(neighbor, visited, component, rev_graph)

    def reverse_graph(g: Dict[int, List[int]]) -> Dict[int, List[int]]:
        reversed_g: Dict[int, List[int]] = defaultdict(list)
        for node in g:
            for neighbor in g[node]:
                reversed_g[neighbor].append(node)
        return dict(reversed_g)

    # First DFS pass
    visited: Set[int] = set()
    stack: List[int] = []
    for node in graph:
        if node not in visited:
            dfs_first(node, visited, stack)

    # Reverse graph
    reversed_graph = reverse_graph(graph)
    
    # Second DFS pass
    sccs: List[List[int]] = []
    visited.clear()

    while stack:
        node = stack.pop()
        if node not in visited:
            component: List[int] = []
            dfs_second(node, visited, component, reversed_graph)
            sccs.append(component)

    return sccs

# Example usage
if __name__ == "__main__":
    print("2-SAT Problem Solver")
    print("=" * 60)
    
    # Example 1: Satisfiable formula
    print("\nExample 1: Satisfiable formula")
    print("Formula: (x1 OR x2) AND (NOT x1 OR x3) AND (NOT x2 OR NOT x3) AND (x2 OR NOT x3)")
    clauses1 = [
        (1, 2),      # x1 OR x2
        (-1, 3),     # NOT x1 OR x3
        (-2, -3),    # NOT x2 OR NOT x3
        (2, -3)      # x2 OR NOT x3
    ]
    num_vars1 = 3
    
    result1 = two_sat_solver(clauses1, num_vars1)
    print(f"Result: {'Satisfiable ✓' if result1 else 'Unsatisfiable ✗'}")
    if result1:
        print("One valid assignment: x1=False, x2=True, x3=False")
    
    # Example 2: Unsatisfiable formula
    print("\n" + "=" * 60)
    print("Example 2: Unsatisfiable formula")
    print("Formula: (x1 OR x2) AND (x1 OR NOT x2) AND (NOT x1 OR x2) AND (NOT x1 OR NOT x2)")
    clauses2 = [
        (1, 2),      # x1 OR x2
        (1, -2),     # x1 OR NOT x2
        (-1, 2),     # NOT x1 OR x2
        (-1, -2)     # NOT x1 OR NOT x2
    ]
    num_vars2 = 2
    
    result2 = two_sat_solver(clauses2, num_vars2)
    print(f"Result: {'Satisfiable ✓' if result2 else 'Unsatisfiable ✗'}")
    if not result2:
        print("Explanation: These clauses force contradictory requirements")
        print("  x1=True requires x2=True AND x2=False (impossible!)")
        print("  x1=False requires x2=True AND x2=False (impossible!)")
    
    # Example 3: Simple satisfiable
    print("\n" + "=" * 60)
    print("Example 3: Simple satisfiable formula")
    print("Formula: (x1 OR x2) AND (NOT x1 OR NOT x2)")
    clauses3 = [
        (1, 2),      # x1 OR x2 (at least one is true)
        (-1, -2)     # NOT x1 OR NOT x2 (at least one is false)
    ]
    num_vars3 = 2
    
    result3 = two_sat_solver(clauses3, num_vars3)
    print(f"Result: {'Satisfiable ✓' if result3 else 'Unsatisfiable ✗'}")
    if result3:
        print("Valid assignments: x1=True, x2=False OR x1=False, x2=True")