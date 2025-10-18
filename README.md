# Graph Theory Algorithms and Examples

This repository contains small, runnable Python scripts that demonstrate common graph data structures and algorithms, plus a couple of simple OOP examples.

- Unweighted graph traversals: Breadth-First Search (BFS) and Depth-First Search (DFS)
- Shortest paths on weighted graphs: SPFA (Shortest Path Faster Algorithm)
- Graph representations: adjacency list and adjacency matrix
- Simple OOP examples: `student` and `point` classes

## Requirements

- Python 3.8+ (no external dependencies)
- Windows PowerShell examples below use `python3`; if your system uses `python`, substitute accordingly.

## Contents

- `breadth_first_search.py` — BFS traversal on an unweighted graph; returns visitation order as a list.
- `depth_first_search.py` — DFS traversal on an unweighted graph; returns visited nodes as a set.
- `spfa.py` — Shortest paths for weighted (possibly negative) directed graphs; detects negative cycles.
- `representing_graphs.py` — Demonstrates a graph as an adjacency list and an adjacency matrix, with display helpers.
- `creating_classes.py` — Simple `student` class example.
- `point.py` — Simple 2D `point` class with distance computation.

## How to run

All scripts are self-contained and can be executed directly. From the repository root in PowerShell:

```powershell
# BFS (prompts for a start node)
python3 .\breadth_first_search.py

# DFS (prompts for a start node)
python3 .\depth_first_search.py

# SPFA (prompts for a start node)
python3 .\spfa.py

# Graph representations demo
python3 .\representing_graphs.py

# OOP examples
python3 .\creating_classes.py
python3 .\point.py
```

To provide the start node non-interactively, you can pipe it on Windows PowerShell:

```powershell
# Example: BFS starting at 9
"9" | python3 .\breadth_first_search.py

# Example: DFS starting at 0
"0" | python3 .\depth_first_search.py

# Example: SPFA starting at 0
"0" | python3 .\spfa.py
```

## Data formats used

- BFS/DFS graph: adjacency list mapping each node to a list of neighbor nodes
  ```python
  sample_graph = {
      0: [1, 2],
      1: [0, 3, 4],
      2: [0],
      3: [1],
      4: [1, 5],
      5: [4]
  }
  ```
  Note: As written, these are directed edges (only the listed direction exists). If you intend an undirected graph, include edges in both directions.

- SPFA graph: adjacency list mapping each node to a list of `(neighbor, weight)` tuples
  ```python
  sample_graph = {
      0: [(1, 5.0), (2, 4.0)],
      1: [(3, 3.0), (4, 2.0)],
      2: [(1, 6.0)],
      3: [(4, -2.0)],
      4: [(5, 1.0)],
      5: [(3, -1.0)]
  }
  ```

## Return values and outputs

- `breadth_first_search(graph, start_node) -> List[int]`
  - Returns nodes in the exact BFS visitation order.
  - The script prints: `BFS visitation order starting from node X: [...]`.

- `depth_first_search(graph, start_node, visited=None) -> Set[int]`
  - Returns the set of visited nodes. If `start_node` has no outgoing edges in the graph, the result is `{start_node}`.
  - The script prints the visited nodes set.

- `spfa(graph, start_node) -> Dict[int, float]`
  - Returns shortest distances from `start_node` to all nodes encountered.
  - Raises `ValueError` if `start_node` is not in the graph or if a negative-weight cycle is detected. The example script catches this and prints a friendly error.

## Time complexity (big-O)

- BFS: O(V + E)
- DFS: O(V + E)
- SPFA: Often fast in practice; worst-case O(V · E)

Where V is the number of vertices and E is the number of edges.

## Tips and notes

- If `python3` isn’t recognized on your PATH in PowerShell, try `python` instead.
- Sets in Python are unordered; DFS printing a set may appear in any order. If you want a stable printout, print `sorted(visited)`.
- For elapsed time measurements, `time.perf_counter()` (used in BFS) reflects wall-clock time; `time.process_time()` (used in DFS) reflects CPU time only.
- If you want BFS/DFS to operate on undirected graphs, ensure each edge is present in both directions in the adjacency list.

## Next steps (ideas)

- Add unit tests for BFS, DFS, and SPFA with small fixtures.
- Extend `spfa.py` to also return predecessors to reconstruct shortest paths.
- Unify graph input formats and add simple loaders from text/JSON.
