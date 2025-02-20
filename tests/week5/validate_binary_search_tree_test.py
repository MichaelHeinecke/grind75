from grind75.week5.validate_binary_search_tree import TreeNode, Solution


def test_tree_is_valid():
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    actual_result = Solution().isValidBST(root)
    assert actual_result is True


def test_tree_is_invalid():
    root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    actual_result = Solution().isValidBST(root)
    assert actual_result is False
