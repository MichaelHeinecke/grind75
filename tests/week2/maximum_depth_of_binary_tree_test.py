from grind75.week2.maximum_depth_of_binary_tree import Solution, TreeNode
from tests.week1.invert_binary_tree_test import create_binary_tree_from_bfs_list


def test_depth_of_no_tree():
    root = None
    expected_result = 0
    solution = Solution()

    actual_result = solution.maxDepth(root)

    assert actual_result == expected_result


def test_depth_of_tree_with_only_root_node():
    root = TreeNode(0)
    expected_result = 1
    solution = Solution()

    actual_result = solution.maxDepth(root)

    assert actual_result == expected_result


def test_depth_of_tree_with_two_nodes():
    root = TreeNode(1, right=TreeNode(2))
    expected_result = 2
    solution = Solution()

    actual_result = solution.maxDepth(root)

    assert actual_result == expected_result


def test_depth_of_tree_with_multiple_nodes():
    bfs_nodes = [3, 9, 20, None, None, 15, 7]
    root = create_binary_tree_from_bfs_list(bfs_nodes)
    expected_result = 3
    solution = Solution()

    actual_result = solution.maxDepth(root)

    assert actual_result == expected_result
