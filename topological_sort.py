"""
Topological Sort for Directed Acyclic Graphs (DAG)

"""

from collections import deque
from typing import Dict, List, Set, Optional, Deque


def topological_sort_kahn(graph: Dict[int, List[int]]) -> Optional[List[int]]:
    """
    Perform topological sort using Kahn's algorithm (BFS-based).
    """
    # Collect all vertices
    vertices: Set[int] = set(graph.keys())
    for neighbors in graph.values():
        vertices.update(neighbors)
    
    # Calculate in-degrees
    in_degree: Dict[int, int] = {v: 0 for v in vertices}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    # Initialize queue with vertices having in-degree 0
    queue: Deque[int] = deque([v for v in vertices if in_degree[v] == 0])
    topo_order: List[int] = []
    
    while queue:
        u: int = queue.popleft()
        topo_order.append(u)
        
        # Reduce in-degree for neighbors
        for v in graph.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # Check if all vertices were processed (no cycle)
    if len(topo_order) == len(vertices):
        return topo_order
    else:
        return None  # Cycle detected


def topological_sort_dfs(graph: Dict[int, List[int]]) -> Optional[List[int]]:
    """
    Perform topological sort using DFS (post-order traversal).
    

    """
    # Collect all vertices
    vertices: Set[int] = set(graph.keys())
    for neighbors in graph.values():
        vertices.update(neighbors)
    
    # States: 0 = unvisited, 1 = visiting, 2 = visited
    state: Dict[int, int] = {v: 0 for v in vertices}
    topo_order: List[int] = []
    has_cycle: bool = False
    
    def dfs(u: int) -> None:
        nonlocal has_cycle
        
        if has_cycle:
            return
        
        if state[u] == 1:  # Back edge found = cycle
            has_cycle = True
            return
        
        if state[u] == 2:  # Already processed
            return
        
        state[u] = 1  # Mark as visiting
        
        for v in graph.get(u, []):
            dfs(v)
        
        state[u] = 2  # Mark as visited
        topo_order.append(u)  # Post-order: add after all descendants
    
    # Process all vertices
    for vertex in vertices:
        if state[vertex] == 0:
            dfs(vertex)
            if has_cycle:
                return None
    
    # Reverse to get correct topological order
    topo_order.reverse()
    return topo_order


def has_cycle(graph: Dict[int, List[int]]) -> bool:
    """
    Check if a directed graph has a cycle.
    

    """
    vertices: Set[int] = set(graph.keys())
    for neighbors in graph.values():
        vertices.update(neighbors)
    
    # States: 0 = unvisited, 1 = visiting, 2 = visited
    state: Dict[int, int] = {v: 0 for v in vertices}
    
    def dfs(u: int) -> bool:
        if state[u] == 1:  # Back edge = cycle
            return True
        if state[u] == 2:  # Already processed
            return False
        
        state[u] = 1  # Mark as visiting
        
        for v in graph.get(u, []):
            if dfs(v):
                return True
        
        state[u] = 2  # Mark as visited
        return False
    
    # Check all components
    for vertex in vertices:
        if state[vertex] == 0:
            if dfs(vertex):
                return True
    
    return False


def all_topological_sorts(graph: Dict[int, List[int]]) -> List[List[int]]:
 
    
    vertices: Set[int] = set(graph.keys())
    for neighbors in graph.values():
        vertices.update(neighbors)
    
    # Calculate in-degrees
    in_degree: Dict[int, int] = {v: 0 for v in vertices}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    result: List[List[int]] = []
    current_order: List[int] = []
    
    def backtrack() -> None:
        if len(current_order) == len(vertices):
            result.append(current_order[:])
            return
        
        # Try all vertices with in-degree 0
        for v in vertices:
            if in_degree[v] == 0 and v not in current_order:
                # Choose vertex v
                current_order.append(v)
                in_degree[v] = -1  # Mark as used
                
                # Reduce in-degrees of neighbors
                saved_degrees: List[int] = []
                for neighbor in graph.get(v, []):
                    saved_degrees.append(in_degree[neighbor])
                    in_degree[neighbor] -= 1
                
                # Recurse
                backtrack()
                
                # Backtrack: restore state
                for i, neighbor in enumerate(graph.get(v, [])):
                    in_degree[neighbor] = saved_degrees[i]
                
                in_degree[v] = 0
                current_order.pop()
    
    backtrack()
    return result


# Example usage
if __name__ == "__main__":
    print("Topological Sort Demo")
    print("=" * 60)
    
    # Example 1: Course prerequisites
    print("\nExample 1: Course Prerequisites")
    courses: Dict[int, List[int]] = {
        0: [1, 2],    # Course 0 is prerequisite for 1 and 2
        1: [3],       # Course 1 is prerequisite for 3
        2: [3],       # Course 2 is prerequisite for 3
        3: [4],       # Course 3 is prerequisite for 4
        4: []         # Course 4 has no dependents
    }
    
    print("Dependencies:")
    for course, prereqs in courses.items():
        if prereqs:
            print(f"  Course {course} must be taken before: {prereqs}")
    
    kahn_order = topological_sort_kahn(courses)
    dfs_order = topological_sort_dfs(courses)
    
    print(f"\nValid course order (Kahn's): {kahn_order}")
    print(f"Valid course order (DFS):    {dfs_order}")
    
    # Example 2: Build dependencies
    print("\n" + "=" * 60)
    print("Example 2: Build System Dependencies")
    build_graph: Dict[int, List[int]] = {
        0: [2, 3],    # main.o depends on lib.o and util.o
        1: [3],       # test.o depends on util.o
        2: [],        # lib.o has no dependencies
        3: []         # util.o has no dependencies
    }
    
    files = {0: "main.o", 1: "test.o", 2: "lib.o", 3: "util.o"}
    
    print("Build dependencies:")
    for file_id, deps in build_graph.items():
        if deps:
            dep_names = [files[d] for d in deps]
            print(f"  {files[file_id]} needs: {dep_names}")
    
    build_order = topological_sort_kahn(build_graph)
    if build_order:
        build_files = [files[i] for i in build_order]
        print(f"\nBuild order: {build_files}")
    
    # Example 3: Cycle detection
    print("\n" + "=" * 60)
    print("Example 3: Cycle Detection")
    cyclic_graph: Dict[int, List[int]] = {
        0: [1],
        1: [2],
        2: [0]  # Creates a cycle: 0 -> 1 -> 2 -> 0
    }
    
    print("Graph with cycle: 0 -> 1 -> 2 -> 0")
    result = topological_sort_kahn(cyclic_graph)
    
    if result is None:
        print("✓ Correctly detected: Cannot perform topological sort (cycle exists)")
        print(f"  has_cycle() returns: {has_cycle(cyclic_graph)}")
    
    # Example 4: All topological orderings
    print("\n" + "=" * 60)
    print("Example 4: All Valid Orderings")
    small_dag: Dict[int, List[int]] = {
        0: [2],
        1: [2],
        2: []
    }
    
    print("DAG: 0 -> 2, 1 -> 2")
    all_orders = all_topological_sorts(small_dag)
    print(f"All valid topological orderings ({len(all_orders)} total):")
    for order in all_orders:
        print(f"  {order}")
