from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time-complexity: O(n)
# Space-complexity: O(h)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False

            return (
                left.val == right.val
                and dfs(left.left, right.right)
                and dfs(left.right, right.left)
            )

        if not root:
            return True
        return dfs(root.left, root.right)
