# Given a binary search tree (BST), find the lowest common ancestor (LCA) node
# of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        current_node = root

        while current_node:
            if p.val < current_node.val and q.val < current_node.val:
                current_node = current_node.left
            elif p.val > current_node.val and q.val > current_node.val:
                current_node = current_node.right
            else:
                return current_node
