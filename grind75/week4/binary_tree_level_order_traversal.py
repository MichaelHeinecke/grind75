from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            level_rep = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level_rep.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level_rep:
                res.append(level_rep)

        return res
