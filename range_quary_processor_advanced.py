"""
efficient range query processing for real-time data
Specialized in handling large datasets with optimized search algorithms
"""
from typing import List


"""
Advanced Range Query Processor with Segment Tree and Fenwick Tree
functions:
- build_segment_tree(data: List[float]) -> None
- range_query_segment(query_start: int, query_end: int) -> float
- build_fenwick_tree(data: List[float]) -> None
- range_query_fenwick(query_start: int, query_end: int) -> float
- real_time_update(index: int, new_value: float) -> None

build_segment_tree: Builds a segment tree for range sum queries.
range_query_segment: Performs range sum query using segment tree.
build_fenwick_tree: Builds a Fenwick Tree (Binary Indexed Tree).
range_query_fenwick: Performs range sum query using Fenwick Tree.
real_time_update: Updates the value at a specific index in real-time.
"""

class RangeQueryProcessorAdvanced:
    def __init__(self, data=None):
        self.data = data or []
        self.segment_tree = None
        self.fenwick_tree = None

    def build_segment_tree(self, data):
        """Build segment tree for range sum queries"""
        n = len(data)
        self.data = data
        self.segment_tree = [0] * (4 * n)
        self._build_segment_tree_util(0, n-1, 0)

    def _build_segment_tree_util(self, start, end, index):
        if start == end:
            self.segment_tree[index] = self.data[start]
            return
        
        mid = (start + end) // 2
        self._build_segment_tree_util(start, mid, 2*index+1)
        self._build_segment_tree_util(mid+1, end, 2*index+2)
        self.segment_tree[index] = self.segment_tree[2*index+1] + self.segment_tree[2*index+2]


    def range_query_segment(self, query_start, query_end):
        """Range sum query using segment tree"""
        return self._range_query_util(0, len(self.data)-1, query_start, query_end, 0)

    def _range_query_util(self, segment_start, segment_end, query_start, query_end, index):
        if query_start <= segment_start and query_end >= segment_end:
            return self.segment_tree[index]
        
        if query_end < segment_start or query_start > segment_end:
            return 0
        
        mid = (segment_start + segment_end) // 2
        left_sum = self._range_query_util(segment_start, mid, query_start, query_end, 2*index+1)
        right_sum = self._range_query_util(mid+1, segment_end, query_start, query_end, 2*index+2)
        return left_sum + right_sum

    def build_fenwick_tree(self, data):
        """Build Fenwick Tree (Binary Indexed Tree)"""
        n = len(data)
        self.data = data
        self.fenwick_tree = [0] * (n + 1)
        
        for i in range(n):
            self._fenwick_update(i, data[i])

    def _fenwick_update(self, index, value):
        index += 1
        while index <= len(self.data):
            self.fenwick_tree[index] += value
            index += index & -index

    def range_query_fenwick(self, query_start, query_end):
        """Range sum query using Fenwick Tree"""
        if query_start == 0:
            return self._fenwick_prefix_sum(query_end)
        return self._fenwick_prefix_sum(query_end) - self._fenwick_prefix_sum(query_start - 1)

    def _fenwick_prefix_sum(self, index):
        """Calculate prefix sum [0..index]"""
        index += 1
        result = 0
        while index > 0:
            result += self.fenwick_tree[index]
            index -= index & -index
        return result

    def real_time_update(self, index, new_value):
        """Update value in real-time for both trees"""
        if index < 0 or index >= len(self.data):
            return
        
        old_value = self.data[index]
        self.data[index] = new_value
        
        # Update segment tree
        if self.segment_tree:
            self._segment_tree_update(0, len(self.data)-1, index, new_value - old_value, 0)
        
        # Update Fenwick tree
        if self.fenwick_tree:
            self._fenwick_update(index, new_value - old_value)

    def _segment_tree_update(self, segment_start, segment_end, update_index, diff, tree_index):
        if update_index < segment_start or update_index > segment_end:
            return
        
        self.segment_tree[tree_index] += diff
        if segment_start != segment_end:
            mid = (segment_start + segment_end) // 2
            self._segment_tree_update(segment_start, mid, update_index, diff, 2*tree_index+1)
            self._segment_tree_update(mid+1, segment_end, update_index, diff, 2*tree_index+2)

# Example usage:
if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11]
    processor = RangeQueryProcessorAdvanced()
    
    # Segment Tree
    processor.build_segment_tree(data)
    print("Segment Tree Range Query (1-4):", processor.range_query_segment(1, 4))  # Output: 24
    
    # Fenwick Tree
    processor.build_fenwick_tree(data)
    print("Fenwick Tree Range Query (1-4):", processor.range_query_fenwick(1, 4))  # Output: 24
    
    # Real-time update
    processor.real_time_update(3, 10)  # Update index 3 from 7 to 10
    print("After Update - Segment Tree Range Query (1-4):", processor.range_query_segment(1, 4))  # Output: 27
    print("After Update - Fenwick Tree Range Query (1-4):", processor.range_query_fenwick(1, 4))  # Output: 27
    
