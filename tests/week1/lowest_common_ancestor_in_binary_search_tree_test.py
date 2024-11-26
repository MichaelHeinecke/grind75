from grind75.week1.lowest_common_ancestor_in_binary_search_tree import (
    Solution,
    TreeNode,
)
from tests.week1.invert_binary_tree_test import create_binary_tree_from_bfs_list


def test_search_nodes_at_same_depth():
    nodes = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    root = create_binary_tree_from_bfs_list(nodes)
    p, q = TreeNode(2), TreeNode(8)
    lowest_common_ancestor = TreeNode(6)

    solution = Solution()
    assert solution.lowestCommonAncestor(root, p, q).val == lowest_common_ancestor.val


def test_lowest_common_ancestor_is_search_node():
    nodes = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    root = create_binary_tree_from_bfs_list(nodes)
    p, q = TreeNode(2), TreeNode(4)
    lowest_common_ancestor = TreeNode(2)

    solution = Solution()
    assert solution.lowestCommonAncestor(root, p, q).val == lowest_common_ancestor.val


def test_search_in_tree_with_only_two_nodes():
    nodes = [2, 1]
    root = create_binary_tree_from_bfs_list(nodes)
    p, q = TreeNode(2), TreeNode(1)
    lowest_common_ancestor = TreeNode(2)

    solution = Solution()
    assert solution.lowestCommonAncestor(root, p, q).val == lowest_common_ancestor.val
