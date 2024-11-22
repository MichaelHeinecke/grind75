from grind75.week1.invert_binary_tree import TreeNode, Solution


def create_binary_tree_from_bfs_list(values: [int | None]) -> TreeNode | None:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while i < len(values):
        current = queue.pop(0)
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root


def get_bfs_representation_of_tree(root: TreeNode | None) -> list[int]:
    rep = []
    if root is None:
        return rep

    queue = [root]

    while queue:
        current = queue.pop(0)
        if current is not None:
            rep.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            rep.append(None)

    while rep and rep[-1] is None:
        rep.pop()

    return rep


def test_no_tree_returns_none():
    values = []
    expected_bfs_rep = []
    root = create_binary_tree_from_bfs_list(values)

    solution = Solution()
    actual_bfs_rep = get_bfs_representation_of_tree(solution.invertTree(root))
    assert actual_bfs_rep == expected_bfs_rep


def test_single_node_is_inverted_correctly():
    values = [2, 1, 3]
    expected_bfs_rep = [2, 3, 1]
    root = create_binary_tree_from_bfs_list(values)

    solution = Solution()
    inverted_tree = solution.invertTree(root)
    actual_bfs_rep = get_bfs_representation_of_tree(inverted_tree)
    assert actual_bfs_rep == expected_bfs_rep


def test_tree_is_inverted_correctly():
    values = [4, 2, 7, 1, 3, 6, 9]
    expected_bfs_rep = [4, 7, 2, 9, 6, 3, 1]
    root = create_binary_tree_from_bfs_list(values)

    solution = Solution()
    actual_bfs_rep = get_bfs_representation_of_tree(solution.invertTree(root))
    assert actual_bfs_rep == expected_bfs_rep
