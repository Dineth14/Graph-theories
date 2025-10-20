"""
Efficient range query processing for real-time data
Specialized in handling large datasets with optimized search algorithms

functions:
- range_query(low: float, high: float) -> List[float]

range_query: Returns all elements within the specified range [low, high].
"""

from typing import List


class RangeQueryProcessor:
    def __init__(self, data: List[float]):
        self.data = sorted(data)

    def range_query(self, low: float, high: float) -> List[float]:
        """Return all elements within the specified range [low, high]."""
        result = []
        for value in self.data:
            if low <= value <= high:
                result.append(value)
            elif value > high:
                break
        return result
    

    
# Example usage:
if __name__ == "__main__":
    data = [1.5, 3.2, 4.8, 7.1, 9.0, 10.5]
    processor = RangeQueryProcessor(data)
    result = processor.range_query(4.0, 9.0)
    print("Range Query Result:", result)  # Output: Range Query Result: [4.8, 7.1, 9.0]    

