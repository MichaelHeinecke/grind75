from grind75.week2.middle_of_linked_list import ListNode, Solution


def test_middleNode_odd():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    solution = Solution()

    middle = solution.middleNode(head)

    assert middle.val == 3


def test_middleNode_even():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    solution = Solution()

    middle = solution.middleNode(head)

    assert middle.val == 4


def test_middleNode_single():
    head = ListNode(1)
    solution = Solution()

    middle = solution.middleNode(head)

    assert middle.val == 1


def test_middleNode_two():
    head = ListNode(1, ListNode(2))
    solution = Solution()

    middle = solution.middleNode(head)

    assert middle.val == 2


def test_middleNode_none():
    head = None
    solution = Solution()

    middle = solution.middleNode(head)

    assert middle is None
