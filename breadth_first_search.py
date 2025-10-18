"""
Breadth-First Search (BFS) Algorithm Implementation
This module provides an implementation of the Breadth-First Search (BFS) algorithm for traversing or searching tree or graph data structures.
It includes a function to perform BFS and an example usage of the function.
"""

import time
from collections import deque
from typing import Dict, List, Set

"""BFS function definition
the breadth_first_search function performs a breadth-first traversal of a graph starting from a specified node.it uses a queue to explore all neighbors at the present depth prior to moving on to nodes at the next depth level.
it takes two parameters:      
- graph: A dictionary representing the adjacency list of the graph.
- start_node: The node from which to start the BFS traversal.
"""

def breadth_first_search(graph: Dict[int, List[int]], start_node: int) -> List[int]:
    """Perform BFS and return the nodes in visitation order.
    Returns a list with the order nodes were visited. This is often more useful
    than a set when the traversal sequence matters.
    param graph: Dict[int, List[int]]: The adjacency list of the graph.
    param start_node: int: The node from which to start the BFS traversal.
    """
    visited: Set[int] = set()  # A set to keep track of visited nodes.
    order: List[int] = []      # A list to record the order of visited nodes.
    queue = deque([start_node])# Queue for BFS traversal.
    visited.add(start_node)

    while queue:
        current_node = queue.popleft()
        order.append(current_node)
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

# Example usage
if __name__ == "__main__":
    # Defining a sample graph using an adjacency list
    sample_graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0],
        3: [1],
        4: [1, 5],
        5: [4],
        6: [7],
        7: [6],
        8: [5, 9],
        9: [3, 4, 7]
    }

    #custom input 
    start_node = int(input("Enter the start node for BFS: "))
    time_start = time.perf_counter()

    # Performing BFS starting from the user-defined start_node
    visited_order = breadth_first_search(sample_graph, start_node=start_node)
    print(f"BFS visitation order starting from node {start_node}: {visited_order}")
    print("BFS traversal complete.")
    print("time Taken for BFS:", time.perf_counter() - time_start, "seconds")
