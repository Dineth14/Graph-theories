"""
longest path in a tree.
the diameter is defined as the length of the longest path between any two nodes in the tree.

functions:
- calculate_longest_paths(root: TreeNode) -> dict
- calculate_max_lengths_from_children(node: TreeNode) -> int
- calculate_max_lengths_from_parent(node: TreeNode) -> None

calculate_longest_paths: Calculate the longest path from each node in the tree.
calculate_max_lengths_from_children: Helper function to compute max lengths from children.
calculate_max_lengths_from_parent: Helper function to compute max lengths from parent.

"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None
        self.max_length_from_children = 0
        self.second_max_length_from_children = 0
        self.max_length_from_parent = 0

"""Calculate the longest path from each node in the tree.

theory:
- The longest path in a tree can be found using a depth-first search (DFS) approach.
- We can calculate the longest path from each node by considering the maximum lengths from its children and its parent.
- This involves two main steps: calculating the maximum lengths from children and then from the parent.
- Finally, we combine these lengths to get the longest path for each node.
"""
def calculate_max_lengths_from_children(node: TreeNode) -> int:
    if not node:
        return 0
    
    max_lengths = [0, 0]  # Store the top two lengths
    for child in node.children:
        child_length = calculate_max_lengths_from_children(child)
        if child_length > max_lengths[0]:
            max_lengths[1] = max_lengths[0]
            max_lengths[0] = child_length
        elif child_length > max_lengths[1]:
            max_lengths[1] = child_length
    
    node.max_length_from_children = max_lengths[0]
    node.second_max_length_from_children = max_lengths[1]
    
    return node.max_length_from_children + 1

def calculate_max_lengths_from_parent(node: TreeNode):
    if not node:
        return
    
    for child in node.children:
        if node.max_length_from_children == child.max_length_from_children + 1:
            child.max_length_from_parent = max(node.second_max_length_from_children + 1, node.max_length_from_parent + 1)
        else:
            child.max_length_from_parent = max(node.max_length_from_children + 1, node.max_length_from_parent + 1)
        
        calculate_max_lengths_from_parent(child)

def calculate_longest_paths(root: TreeNode) -> dict:
    calculate_max_lengths_from_children(root)
    root.max_length_from_parent = 0
    calculate_max_lengths_from_parent(root)
    
    longest_paths = {}
    
    def collect_longest_paths(node: TreeNode):
        if not node:
            return
        longest_paths[node.value] = max(node.max_length_from_children, node.max_length_from_parent)
        for child in node.children:
            collect_longest_paths(child)
    
    collect_longest_paths(root)
    
    return longest_paths

# Example usage:
if __name__ == "__main__":
    # Construct a sample tree
    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    child3 = TreeNode(4)
    root.children = [child1, child2, child3]
    child1.parent = root
    child2.parent = root
    child3.parent = root
    child1.children = [TreeNode(5), TreeNode(6)]
    child1.children[0].parent = child1
    child1.children[1].parent = child1
    child3.children = [TreeNode(7)]
    child3.children[0].parent = child3

    longest_paths = calculate_longest_paths(root)
    for node_value, length in longest_paths.items():
        print(f"Longest path from node {node_value}: {length}")
