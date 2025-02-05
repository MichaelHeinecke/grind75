from grind75.week3.subtree_of_another_tree import TreeNode, Solution


def test_subtree_in_tree():
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    sub_root = TreeNode(4, TreeNode(1), TreeNode(2))
    expected_result = True

    actual_result = Solution().isSubtree(root, sub_root)

    assert actual_result == expected_result


def test_subtree_not_in_tree():
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
    sub_root = TreeNode(4, TreeNode(1), TreeNode(2))
    expected_result = False

    actual_result = Solution().isSubtree(root, sub_root)

    assert actual_result == expected_result


def test_single_node_with_repeated_value_subtree_in_tree():
    root = TreeNode(1, TreeNode(1))
    sub_root = TreeNode(1)
    expected_result = True

    actual_result = Solution().isSubtree(root, sub_root)

    assert actual_result == expected_result


def test_subtree_not_in_tree_2():
    root = TreeNode(3, TreeNode(4, TreeNode(1)), TreeNode(5, TreeNode(2)))
    sub_root = TreeNode(3, TreeNode(1), TreeNode(2))
    expected_result = False

    actual_result = Solution().isSubtree(root, sub_root)

    assert actual_result == expected_result
