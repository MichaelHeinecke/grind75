from grind75.week2.reverse_linked_list import ListNode, Solution


def test_no_node_to_reverse():
    head = None
    solution = Solution()

    actual_result = solution.reverseList(head)

    assert head == actual_result


def test_reverse_single_node():
    head = ListNode(1, None)
    solution = Solution()

    actual_result = solution.reverseList(head)

    assert head == actual_result


def test_reverse_multiple_nodes():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    solution = Solution()
    expected_result = ListNode(
        5, ListNode(4, ListNode(3, ListNode(2, ListNode(1, None))))
    )

    actual_result = solution.reverseList(head)

    assert actual_result == expected_result


def test_no_node_to_reverse_recursively():
    head = None
    solution = Solution()

    actual_result = solution.reverseListRecursively(head)

    assert head == actual_result


def test_reverse_single_node_recursively():
    head = ListNode(1, None)
    solution = Solution()

    actual_result = solution.reverseListRecursively(head)

    assert head == actual_result


def test_reverse_multiple_nodes_recursively():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    solution = Solution()
    expected_result = ListNode(
        5, ListNode(4, ListNode(3, ListNode(2, ListNode(1, None))))
    )

    actual_result = solution.reverseListRecursively(head)

    assert actual_result == expected_result
