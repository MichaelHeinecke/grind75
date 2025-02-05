from grind75.week3.convert_sorted_array_to_binary_search_tree import Solution
from tests.week1.invert_binary_tree_test import get_bfs_representation_of_tree


def test_array_to_binary_search_tree_1():
    nums = [-10, -3, 0, 5, 9]
    expected_result = [0, -10, 5, None, -3, None, 9]

    actual_tree = Solution().sortedArrayToBST(nums)
    actual_result = get_bfs_representation_of_tree(actual_tree)

    assert actual_result == expected_result


def test_array_to_binary_search_tree_2():
    nums = [1, 3]
    expected_result = [1, None, 3]

    actual_tree = Solution().sortedArrayToBST(nums)
    actual_result = get_bfs_representation_of_tree(actual_tree)

    assert actual_result == expected_result
