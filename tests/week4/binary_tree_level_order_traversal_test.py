import pytest

from grind75.week4.binary_tree_level_order_traversal import Solution
from tests.week1.invert_binary_tree_test import create_binary_tree_from_bfs_list


@pytest.mark.parametrize(
    "bfs_rep, expected_result",
    [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        (None, []),
    ],
)
def test_binary_tree_level_order_traversal(bfs_rep, expected_result):
    root = create_binary_tree_from_bfs_list(bfs_rep)
    actual_result = Solution().levelOrder(root)
    assert actual_result == expected_result
