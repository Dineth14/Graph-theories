"""
Real-time graph analysis engine for hackathon
Specialized in dynamic graphs, centrality measures, and relationship analysis
"""

from typing import List, Dict, Any
import networkx as nx

"""
Dynamic Graph Engine for Real-time Analysis
this engine supports dynamic graph structures, centrality measures, and relationship analysis.
functions:
- add_edge(node1: str, node2: str, timestamp: float) -> None
- remove_edge(node1: str, node2: str) -> None
- get_centrality_measures() -> Dict[str, Any]
- get_relationships(node: str) -> List[str]
- get_time_series_data() -> List[tuple]

add_edge: Adds an edge to the graph with a timestamp.
remove_edge: Removes an edge from the graph.
get_centrality_measures: Returns various centrality measures.
get_relationships: Returns all relationships (neighbors) of a given node.
get_time_series_data: Returns the time series data of edges added.
"""
class DynamicGraphEngine:
    def __init__(self):
        self.graph = nx.Graph()
        self.time_series_data = []

    def add_edge(self, node1: str, node2: str, timestamp: float):
        """Add an edge to the graph with a timestamp."""
        self.graph.add_edge(node1, node2, timestamp=timestamp)
        self.time_series_data.append((timestamp, node1, node2))

    def remove_edge(self, node1: str, node2: str):
        """Remove an edge from the graph."""
        if self.graph.has_edge(node1, node2):
            self.graph.remove_edge(node1, node2)

    def get_centrality_measures(self) -> Dict[str, Any]:
        """Calculate and return various centrality measures."""
        centrality_measures = {
            'degree_centrality': nx.degree_centrality(self.graph),
            'betweenness_centrality': nx.betweenness_centrality(self.graph),
            'closeness_centrality': nx.closeness_centrality(self.graph),
            'eigenvector_centrality': nx.eigenvector_centrality(self.graph)
        }
        return centrality_measures

    def get_relationships(self, node: str) -> List[str]:
        """Get all relationships (neighbors) of a given node."""
        if self.graph.has_node(node):
            return list(self.graph.neighbors(node))
        return []

    def get_time_series_data(self) -> List[tuple]:
        """Return the time series data of edges added."""
        return sorted(self.time_series_data, key=lambda x: x[0])
    
# Example usage:
if __name__ == "__main__":
    engine = DynamicGraphEngine()
    engine.add_edge("A", "B", timestamp=1.0)
    engine.add_edge("B", "C", timestamp=2.0)
    engine.add_edge("A", "C", timestamp=3.0)

    print("Centrality Measures:", engine.get_centrality_measures())
    print("Relationships of B:", engine.get_relationships("B"))
    print("Time Series Data:", engine.get_time_series_data())

  

