from collections import deque
from typing import Optional, List, Any

import pytest

from grind75.week5.clone_graph import Node, Solution


def build_graph(adj_list: List[List[int]]) -> Optional[Node]:
    if not adj_list:
        return None
    nodes = [Node(i + 1) for i in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0]


def build_adjacency_list(node: Optional[Node]) -> list[list[int]]:
    if not node:
        return []

    adj_dct = {}
    queue = deque([node])
    visited = set()

    while queue:
        current = queue.popleft()
        if current.val not in visited:
            visited.add(current.val)
            adj_dct[current.val] = [neighbor.val for neighbor in current.neighbors]
            for neighbor in current.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)

    return [adj_dct[i] for i in sorted(adj_dct)]


@pytest.mark.parametrize(
    "adj_list, expected_adj_list",
    [
        ([[2, 4], [1, 3], [2, 4], [1, 3]], [[2, 4], [1, 3], [2, 4], [1, 3]]),
        ([[]], [[]]),
        ([], []),
    ],
)
def test_clone_graph(adj_list, expected_adj_list):
    original = build_graph(adj_list)
    cloned = Solution().cloneGraph(original)
    actual_adj_list = build_adjacency_list(cloned)
    assert actual_adj_list == expected_adj_list
