from grind75.week3.symmetric_tree import Solution
from tests.week1.invert_binary_tree_test import create_binary_tree_from_bfs_list


def test_tree_is_symmetric():
    bfs_rep = [1, 2, 2, 3, 4, 4, 3]
    root = create_binary_tree_from_bfs_list(bfs_rep)

    actual_result = Solution().isSymmetric(root)

    assert actual_result is True


def test_tree_is_not_symmetric():
    bfs_rep = [1, 2, 2, None, 3, None, 3]
    root = create_binary_tree_from_bfs_list(bfs_rep)

    actual_result = Solution().isSymmetric(root)

    assert actual_result is False


def test_empty_tree_is_symmetric():
    root = None

    actual_result = Solution().isSymmetric(root)

    assert actual_result is True
