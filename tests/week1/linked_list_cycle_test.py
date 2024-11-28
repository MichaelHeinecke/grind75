from pytest import fixture

from grind75.week1.linked_list_cycle import ListNode, Solution


@fixture
def solution() -> Solution:
    return Solution()


def test_no_cycle(solution):
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    assert solution.hasCycle(head) is False


def test_cycle(solution):
    head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    head.next = second
    second.next = third
    third.next = second  # Creates a cycle
    assert solution.hasCycle(head) is True


def test_single_node_no_cycle(solution):
    head = ListNode(1)
    assert solution.hasCycle(head) is False


def test_single_node_with_cycle(solution):
    head = ListNode(1)
    head.next = head  # Creates a cycle
    assert solution.hasCycle(head) is True


def test_empty_list(solution):
    assert solution.hasCycle(None) is False
