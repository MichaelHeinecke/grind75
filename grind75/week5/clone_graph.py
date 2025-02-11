from collections import deque
from typing import Optional, Deque, Dict


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        return f"val: {self.val}, neighbors: [{', '.join(str(nei.val) for nei in self.neighbors)}]"


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        copied_nodes: Dict[Node, Node] = {node: Node(node.val)}
        queue: Deque[Node] = deque([node])

        while queue:
            original = queue.popleft()
            copy = copied_nodes[original]

            for neighbor in original.neighbors:
                if neighbor not in copied_nodes:
                    copied_nodes[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                copy.neighbors.append(copied_nodes[neighbor])

        return copied_nodes[node]
