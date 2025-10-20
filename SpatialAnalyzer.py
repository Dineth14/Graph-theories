"""
Spatial data analysis and range queries for geographical data
Specialized in spatial indexing and efficient querying of geographical datasets

"""

from typing import List, Tuple
from sklearn.neighbors import KDTree
from sklearn.cluster import DBSCAN
import numpy as np

"""
Spatial Analyzer for Geographical Data
functions:
- spatial_index(data: List[tuple]) -> None
- range_query(spatial_bounds: tuple) -> List[tuple]
- nearest_neighbors(point: tuple, k: int) -> List[tuple]
- spatial_clustering(eps: float, min_samples: int) -> List[List[tuple]]
- spatial_index: Builds a spatial index for efficient querying.

range_query: Returns all spatial data points within the specified spatial bounds.
nearest_neighbors: Finds the k nearest neighbors of a given point.
spatial_clustering: Performs spatial clustering using DBSCAN algorithm.
spatial_index: Builds a spatial index for efficient querying.

"""
class SpatialAnalyzer:
    def __init__(self):
        self.data = []
        self.kd_tree = None

    def spatial_index(self, data: List[Tuple[float, float]]):
        """Build a spatial index for efficient querying."""
        self.data = data
        self.kd_tree = KDTree(np.array(data))

    def range_query(self, spatial_bounds: Tuple[float, float, float, float]) -> List[Tuple[float, float]]:
        """Return all spatial data points within the specified spatial bounds."""
        if not self.kd_tree:
            return []
        
        x_min, y_min, x_max, y_max = spatial_bounds
        indices = self.kd_tree.query_radius(
            np.array([[ (x_min + x_max) / 2, (y_min + y_max) / 2 ]]),
            r=max(x_max - x_min, y_max - y_min) / 2
        )[0]
        
        result = []
        for idx in indices:
            point = self.data[idx]
            if x_min <= point[0] <= x_max and y_min <= point[1] <= y_max:
                result.append(point)
        
        return result

    def nearest_neighbors(self, point: Tuple[float, float], k: int) -> List[Tuple[float, float]]:
        """Find the k nearest neighbors of a given point."""
        if not self.kd_tree:
            return []
        
        distances, indices = self.kd_tree.query([point], k=k)
        return [self.data[idx] for idx in indices[0]]

    def spatial_clustering(self, eps: float, min_samples: int) -> List[List[Tuple[float, float]]]:
        """Perform spatial clustering using DBSCAN algorithm."""
        if not self.data:
            return []
        
        db = DBSCAN(eps=eps, min_samples=min_samples).fit(np.array(self.data))
        labels = db.labels_
        
        clusters = {}
        for idx, label in enumerate(labels):
            if label == -1:
                continue  # Noise
            if label not in clusters:
                clusters[label] = []
            clusters[label].append(self.data[idx])
        
        return list(clusters.values())
    
# Example usage:
if __name__ == "__main__":
    analyzer = SpatialAnalyzer()
    sample_data = [(1.0, 2.0), (2.5, 4.0), (3.0, 1.5), (5.0, 7.0), (8.0, 8.0)]
    analyzer.spatial_index(sample_data)

    print("Range Query Result:", analyzer.range_query((1.0, 1.0, 4.0, 5.0)))
    print("Nearest Neighbors of (2.0, 3.0):", analyzer.nearest_neighbors((2.0, 3.0), k=2))
    print("Spatial Clustering Result:", analyzer.spatial_clustering(eps=2.0, min_samples=2))

