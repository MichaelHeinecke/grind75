from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def are_identical(
            tree_node: Optional[TreeNode], sub_tree_node: Optional[TreeNode]
        ) -> bool:
            if not tree_node and not sub_tree_node:
                return True
            if tree_node and sub_tree_node and tree_node.val == sub_tree_node.val:
                return are_identical(
                    tree_node.left, sub_tree_node.left
                ) and are_identical(tree_node.right, sub_tree_node.right)
            return False

        if not subRoot:
            return True
        if not root:
            return False
        if are_identical(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
