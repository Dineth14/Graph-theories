"""This module defines a class to represent a student with attributes such as name, age, and grade,"""

# and a method to display the student's information.
class student:
    # Initializing the student class with name, age, and grade
    def __init__(self, name: str, age: int, grade: float) -> None:
        self.name = name
        self.age = age
        self.grade = grade

    # Method to display student information
    def display_info(self) -> None:
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def get_grades(self) -> float:
        return self.grade

# Example usage

if __name__ == "__main__":
    # Creating instances of the student class
    student1 = student("Alice", 20, 88.5)
    student2 = student("Bob", 22, 92.0)
    # Displaying student information
    student1.display_info()
    student2.display_info()

    # Getting and printing student grades
    print(f"{student1.name}'s Grade: {student1.get_grades()}")
    print(f"{student2.name}'s Grade: {student2.get_grades()}")
