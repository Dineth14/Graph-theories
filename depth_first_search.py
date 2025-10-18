"""
Depth-First Search (DFS) Algorithm Implementation
This module provides an implementation of the Depth-First Search (DFS) algorithm for traversing or searching tree or graph data structures.
It includes a function to perform DFS and an example usage of the function.
"""
import sys
import time
from typing import Dict, List, Set

# Increasing recursion limit for deep graphs
sys.setrecursionlimit(10**6)

"""
the depth_first_search function performs a depth-first traversal of a graph starting from a specified node.it uses recursion to explore as far as possible along each branch before backtracking.
it takes three parameters:
- graph: A dictionary representing the adjacency list of the graph.
- start_node: The node from which to start the DFS traversal.
- visited: A set to keep track of visited nodes (used internally during recursion).
"""
# DFS function definition
def depth_first_search(graph: Dict[int, List[int]], start_node: int, visited: Set[int] = None) -> Set[int]:#param graph: Dict[int, List[int]]: The adjacency list of the graph., start_node: int: The node from which to start the DFS traversal., visited: Set[int]: A set to keep track of visited nodes (used internally during recursion).
    if visited is None:
        visited = set()
    visited.add(start_node)
    for neighbor in graph.get(start_node, []):#the method retrieves the list of neighbors for the current start_node from the graph's adjacency list. If the start_node has no neighbors, it defaults to an empty list to avoid errors.
        if neighbor not in visited:
            depth_first_search(graph, neighbor, visited)
    return visited

# Example usage
if __name__ == "__main__":
    # Defining a sample graph using an adjacency list
    sample_graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0],
        3: [1],
        4: [1, 5],
        5: [4]
    }

    #custom input 
    start_node = int(input("Enter the start node for DFS: "))
    time_start = time.process_time()

    # Performing DFS starting from the user-defined start_node
    visited_nodes = depth_first_search(sample_graph, start_node=start_node)
    print(f"Nodes visited in DFS starting from node {start_node}: {visited_nodes}")
    print("DFS traversal complete.")
    print("time Taken for DFS:", time.process_time() - time_start, "seconds")
