from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.is_balanced_dfs(root)[0]

    def is_balanced_dfs(self, node: Optional[TreeNode]) -> (bool, int):
        if not node:
            return True, 0

        left = self.is_balanced_dfs(node.left)
        right = self.is_balanced_dfs(node.right)

        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        height = max(left[1], right[1]) + 1
        return balanced, height