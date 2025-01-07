from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        return self.get_tree_bfs_representation(p) == self.get_tree_bfs_representation(
            q
        )

    def get_tree_bfs_representation(self, root: TreeNode) -> list[Optional[int]]:
        queue: deque[Optional[TreeNode]] = deque([root])
        rep = []

        while queue:
            node = queue.popleft()
            if node:
                rep.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                rep.append(None)

        return rep
