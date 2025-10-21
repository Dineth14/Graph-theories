"""
calculate the diameter of a tree.
the diameter is defined as the length of the longest path between any two nodes in the tree.

"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def tree_diameter(root: TreeNode) -> int:
    """Calculate the diameter of the tree."""
    diameter = 0

    def height_and_diameter(node: TreeNode) -> int:
        nonlocal diameter
        if not node:
            return 0
        
        max_heights = [0, 0]  # Store the top two heights
        for child in node.children:
            child_height = height_and_diameter(child)
            if child_height > max_heights[0]:
                max_heights[1] = max_heights[0]
                max_heights[0] = child_height
            elif child_height > max_heights[1]:
                max_heights[1] = child_height
        
        # Update the diameter if the path through this node is larger
        diameter = max(diameter, max_heights[0] + max_heights[1])
        
        return max_heights[0] + 1  # Height of the current node

    height_and_diameter(root)
    return diameter

# Example usage:
if __name__ == "__main__":
    # Construct a sample tree
    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    child3 = TreeNode(4)
    root.children = [child1, child2, child3]
    child1.children = [TreeNode(5), TreeNode(6)]
    child3.children = [TreeNode(7)]

    print("Diameter of the tree:", tree_diameter(root))



