from grind75.week1.balanced_binary_tree import Solution
from tests.week1.invert_binary_tree_test import create_binary_tree_from_bfs_list


def test_tree_is_balanced():
    nodes = [3, 9, 20, None, None, 15, 7]
    expected_result = True
    root = create_binary_tree_from_bfs_list(nodes)

    solution = Solution()
    result = solution.isBalanced(root)

    assert result == expected_result


def test_tree_is_not_balanced():
    nodes = [1, 2, 2, 3, 3, None, None, 4, 4]
    expected_result = False
    root = create_binary_tree_from_bfs_list(nodes)

    solution = Solution()
    result = solution.isBalanced(root)

    assert result == expected_result


def test_subtree_is_not_balanced_():
    nodes = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]
    expected_result = False
    root = create_binary_tree_from_bfs_list(nodes)

    solution = Solution()
    result = solution.isBalanced(root)

    assert result == expected_result


def test_tree_without_nodes_is_balanced():
    nodes = []
    expected_result = True
    root = create_binary_tree_from_bfs_list(nodes)

    solution = Solution()
    result = solution.isBalanced(root)

    assert result == expected_result
