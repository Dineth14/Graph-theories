# Representing Graphs in computer science

# This code defines a simple undirected graph using an adjacency list representation.

class Graph:
    # Initializing the graph with an empty adjacency list
    def __init__(self, num_nodes: int = 0) -> None:
        self.adjacency_list = {}
        self.num_edges = 0
        self.num_nodes = num_nodes

    # Method to add an edge between two nodes
    """
    this Adds an undirected edge between nodes u and v by updating the adjacency list.the method also increments the edge count and initializes nodes in the adjacency list if they do not already exist.   
    Parameters:
    u (int): The first node.
    v (int): The second node.

    """
    def add_edge(self, u: int, v: int) -> None:
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []  # Initialize list for new node
            self.num_nodes += 1
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []  # Initialize list for new node
            self.num_nodes += 1
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)  # For undirected graph
        self.num_edges += 1

    def display(self) -> None:
        print("Graph adjacency list:")
        for node, edges in self.adjacency_list.items():
            print(f"{node}: {', '.join(map(str, edges))}")
        print(f"Total nodes: {self.num_nodes}, Total edges: {self.num_edges}")

# Alternative representation using adjacency matrix
class GraphMatrix:
    # Initializing the graph with a given size and creating an adjacency matrix
    def __init__(self, size: int) -> None:
        self.size = size
        self.adjacency_matrix = [[0 for _ in range(size)] for _ in range(size)]
        self.num_edges = 0

    # Method to add an edge between two nodes
    """
    Adds an undirected edge between nodes u and v by updating the adjacency matrix. The method also increments the edge count.
    Parameters:
    u (int): The first node.
    v (int): The second node.
    """
    def add_edge(self, u: int, v: int) -> None:
        if u >= self.size or v >= self.size:
            raise ValueError("Node index out of bounds")
        self.adjacency_matrix[u][v] = 1
        self.adjacency_matrix[v][u] = 1  # For undirected graph
        self.num_edges += 1

    def display(self) -> None:
        print("Graph adjacency matrix:")
        for row in self.adjacency_matrix:
            print(' '.join(map(str, row)))
        print(f"Total nodes: {self.size}, Total edges: {self.num_edges}")
        print("Matrix representation complete.")

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.display()

    gm = GraphMatrix(5)
    gm.add_edge(0, 1)
    gm.add_edge(0, 2)
    gm.add_edge(1, 3)
    gm.add_edge(2, 3)
    gm.display()