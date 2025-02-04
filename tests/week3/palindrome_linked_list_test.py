from grind75.week3.palindrome_linked_list import ListNode, Solution


def test_linked_list_is_palindrome():
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))

    actual_result = Solution().isPalindrome(head)

    assert actual_result is True


def test_linked_list_is_not_palindrome():
    head = ListNode(1, ListNode(2))

    actual_result = Solution().isPalindrome(head)

    assert actual_result is False
