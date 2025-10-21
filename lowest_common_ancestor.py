"""
lowest common ancestor (LCA) in a tree.
The lowest common ancestor of two nodes of a rooted tree is the lowest node
whose subtree contains both the nodes. A typical problem is to efficiently process
queries that ask to find the lowest common ancestor of two nodes.

functions:
- lowest_common_ancestor(root: TreeNode, node1: TreeNode, node2: TreeNode) -> TreeNode
- find_path(root: TreeNode, target: TreeNode, path: List[TreeNode]) -> bool

lowest_common_ancestor: Find the lowest common ancestor of two nodes in the tree.
find_path: Helper function to find the path from root to a given target node.

"""

from typing import List, Optional

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def find_path(root: TreeNode, target: TreeNode, path: List[TreeNode]) -> bool:
    """Helper function to find the path from root to a given target node."""
    if root is None:
        return False
    
    path.append(root)
    
    if root == target:
        return True
    
    for child in root.children:
        if find_path(child, target, path):
            return True
    
    path.pop()
    return False

def lowest_common_ancestor(root: TreeNode, node1: TreeNode, node2: TreeNode) -> Optional[TreeNode]:
    """Find the lowest common ancestor of two nodes in the tree."""
    path1 = []
    path2 = []
    
    if not find_path(root, node1, path1) or not find_path(root, node2, path2):
        return None  # One of the nodes is not present in the tree
    
    lca = None
    for u, v in zip(path1, path2):
        if u == v:
            lca = u
        else:
            break
    
    return lca

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

    node1 = child1.children[0]  # Node with value 5
    node2 = child3.children[0]  # Node with value 7

    lca_node = lowest_common_ancestor(root, node1, node2)
    if lca_node:
        print("Lowest Common Ancestor of nodes", node1.value, "and", node2.value, "is:", lca_node.value)
    else:
        print("One or both nodes are not present in the tree.")