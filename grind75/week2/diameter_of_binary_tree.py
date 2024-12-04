from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter: int = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            """Returns the height of a TreeNode"""
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            local_diameter = left + right
            if local_diameter > self.diameter:
                self.diameter = local_diameter

            height = max(left, right) + 1
            return height

        dfs(root)
        return self.diameter
