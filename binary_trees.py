"""
Binary trees
A binary tree is a rooted tree where each node has a left and right subtree. It is
possible that a subtree of a node is empty. Thus, every node in a binary tree has
zero, one or two children.
For example, the following tree is a binary tree:
1
2 3
4 5
6
7
The nodes of a binary tree have three natural orderings that correspond to
different ways to recursively traverse the tree:
• pre-order: first process the root, then traverse the left subtree, then
traverse the right subtree
• in-order: first traverse the left subtree, then process the root, then traverse
the right subtree
• post-order: first traverse the left subtree, then traverse the right subtree,
then process the root
For the above tree, the nodes in pre-order are [1,2,4,5,6,3,7], in in-order
[4,2,6,5,1,3,7] and in post-order [4,6,5,2,7,3,1].
If we know the pre-order and in-order of a tree, we can reconstruct the exact
structure of the tree. For example, the above tree is the only possible tree with
pre-order [1,2,4,5,6,3,7] and in-order [4,2,6,5,1,3,7]. In a similar way, the
post-order and in-order also determine the structure of a tree.
However, the situation is different if we only know the pre-order and postorder of a tree. In this case, there may be more than one tree that match the
orderings. For example, in both of the trees
1
2
1
2
the pre-order is [1,2] and the post-order is [2,1], but the structures of the trees
are different.
"""

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree_from_pre_in(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root_value = preorder[0]
    root = BinaryTreeNode(root_value)
    
    root_index_in_inorder = inorder.index(root_value)
    
    root.left = build_tree_from_pre_in(
        preorder[1:1 + root_index_in_inorder],
        inorder[:root_index_in_inorder]
    )
    
    root.right = build_tree_from_pre_in(
        preorder[1 + root_index_in_inorder:],
        inorder[root_index_in_inorder + 1:]
    )
    
    return root

def build_tree_from_post_in(postorder, inorder):
    if not postorder or not inorder:
        return None
    
    root_value = postorder[-1]
    root = BinaryTreeNode(root_value)
    
    root_index_in_inorder = inorder.index(root_value)
    
    root.left = build_tree_from_post_in(
        postorder[:root_index_in_inorder],
        inorder[:root_index_in_inorder]
    )
    
    root.right = build_tree_from_post_in(
        postorder[root_index_in_inorder:-1],
        inorder[root_index_in_inorder + 1:]
    )
    
    return root

#example usage:
if __name__ == "__main__":
    preorder = [1, 2, 4, 5, 6, 3, 7]
    inorder = [4, 2, 6, 5, 1, 3, 7]
    postorder = [4, 6, 5, 2, 7, 3, 1]

    root_from_pre_in = build_tree_from_pre_in(preorder, inorder)
    root_from_post_in = build_tree_from_post_in(postorder, inorder)
    print("Root from pre-order and in-order:", root_from_pre_in.value)
    print("Root from post-order and in-order:", root_from_post_in.value)