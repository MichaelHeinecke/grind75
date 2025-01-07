from grind75.week3.same_tree import TreeNode, Solution


def test_equal_trees_are_equal():
    root_left = TreeNode(1, TreeNode(2), TreeNode(3))
    root_right = TreeNode(1, TreeNode(2), TreeNode(3))

    actual_result = Solution().isSameTree(root_left, root_right)

    assert actual_result is True


def test_mirrored_trees_are_not_equal():
    root_left = TreeNode(1, left=TreeNode(2))
    root_right = TreeNode(1, right=TreeNode(2))

    actual_result = Solution().isSameTree(root_left, root_right)

    assert actual_result is False


def test_mirrored_trees_are_not_equal_2():
    root_left = TreeNode(1, TreeNode(2), TreeNode(1))
    root_right = TreeNode(1, TreeNode(1), TreeNode(2))

    actual_result = Solution().isSameTree(root_left, root_right)

    assert actual_result is False


def test_empty_trees_are_equal():
    root_left = None
    root_right = None

    actual_result = Solution().isSameTree(root_left, root_right)

    assert actual_result is True
