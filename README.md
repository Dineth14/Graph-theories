# Graph Theory Algorithms and Examples

This repository contains small, runnable Python scripts that demonstrate common graph data structures and algorithms, plus a couple of simple OOP examples.

- Unweighted graph traversals: Breadth-First Search (BFS) and Depth-First Search (DFS)
- Shortest paths on weighted graphs: SPFA (Shortest Path Faster Algorithm)
- Graph representations: adjacency list and adjacency matrix
- Simple OOP examples: `student` and `point` classes

## 📚 Learning Resources

**`graph_theory_tutorial.ipynb`** includes:
- 📖 **Graph fundamentals** - What are graphs? Types, terminology, and real-world examples
- 🗺️ **Graph representations** - Adjacency lists vs matrices with working code examples
- 🔍 **BFS & DFS explained** - Step-by-step walkthroughs with visualizations
- 🛣️ **Shortest path algorithms** - SPFA algorithm with detailed explanations
- 💡 **Practical examples** - Social networks, city navigation, connected components
- 🎯 **When to use what** - Decision guide for choosing the right algorithm

#### How to use the notebook:

1. **Open in VS Code** (recommended):
   - Simply open `graph_theory_tutorial.ipynb` in VS Code
   - VS Code will prompt you to install the Jupyter extension if needed
   - Click "Select Kernel" and choose your Python environment
   - Run cells with Shift+Enter

2. **Or use Jupyter Notebook/Lab**:
   ```powershell
   # Install Jupyter if you don't have it
   pip install jupyter
   
   # Launch Jupyter Notebook
   jupyter notebook graph_theory_tutorial.ipynb
   ```

3. **Or use Google Colab**:
   - Upload the notebook to Google Colab
   - Run it directly in your browser (no installation needed!)

## Requirements

- Python 3.8+ (no external dependencies for scripts)
- For the Jupyter notebook: Jupyter, VS Code with Jupyter extension, or Google Colab
- Windows PowerShell examples below use `python3`; if your system uses `python`, substitute accordingly.


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

## Learning Path

If you're new to graph theory, we recommend this learning path:

1. **Start with the tutorial notebook** (`graph_theory_tutorial.ipynb`)
   - Read through the explanations
   - Run the code cells to see algorithms in action
   - Try modifying the examples

2. **Experiment with the scripts**
   - Run `representing_graphs.py` to understand data structures
   - Try `breadth_first_search.py` and `depth_first_search.py` with different start nodes
   - Test `spfa.py` with various weighted graphs

3. **Practice and build**
   - Modify the example graphs
   - Try creating your own graph problems
   - Implement additional algorithms (Dijkstra, Bellman-Ford, etc.)


