"""
This module defines a class to represent a point in 2D space with x and y coordinates,
and methods to display the point's information and calculate the distance from another point.
"""
class point:

    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y

    def display_coordinates(self) -> None:
        print(f"Point coordinates: ({self.x}, {self.y})")

    def distance(self, other: "point") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

# Example usage
if __name__ == "__main__":
    point1 = point(3, 4)
    point2 = point(6, 8)

    point1.display_coordinates()
    point2.display_coordinates()

    print(f"Distance between points: {point1.distance(point2)}")