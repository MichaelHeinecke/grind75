from grind75.week2.diameter_of_binary_tree import Solution
from tests.week1.invert_binary_tree_test import create_binary_tree_from_bfs_list


def test_single_edge_tree_has_diameter_one():
    bfs_rep = [1, 2]
    root = create_binary_tree_from_bfs_list(bfs_rep)
    expected_result = 1
    solution = Solution()

    actual_result = solution.diameterOfBinaryTree(root)

    assert actual_result == expected_result


def test_multiple_edge_tree_has_diameter_three():
    bfs_rep = [1, 2, 3, 4, 5]
    root = create_binary_tree_from_bfs_list(bfs_rep)
    expected_result = 3
    solution = Solution()

    actual_result = solution.diameterOfBinaryTree(root)

    assert actual_result == expected_result


def test_unbalanced_tree_diameter_is_correclty_calculated():
    bfs_rep = [1, None, 3, 4, 5, 6, 7, 8, 9]
    root = create_binary_tree_from_bfs_list(bfs_rep)
    expected_result = 4
    solution = Solution()

    actual_result = solution.diameterOfBinaryTree(root)

    assert actual_result == expected_result
