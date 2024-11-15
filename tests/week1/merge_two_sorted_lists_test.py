from typing import Optional

from grind75.week1.merge_two_sorted_lists import ListNode, Solution


def vals_to_list(node: Optional[ListNode]):
    res = []

    if not node:
        return res

    res = [node.val]
    pointer = node.next
    while pointer:
        res.append(pointer.val)
        pointer = pointer.next
    return res


def test_two_lists_result_in_merged_list():
    solution = Solution()
    input_list_1 = ListNode(
        val=1, next=ListNode(val=2, next=ListNode(val=4, next=None))
    )
    input_list_2 = ListNode(
        val=1, next=ListNode(val=3, next=ListNode(val=4, next=None))
    )
    expected_merged_list = [1, 1, 2, 3, 4, 4]

    actual_merged_list = vals_to_list(
        solution.merge_two_lists(input_list_1, input_list_2)
    )
    assert actual_merged_list == expected_merged_list


def test_two_empty_lists_result_in_empty_list():
    solution = Solution()
    input_list_1 = None
    input_list_2 = None
    expected_merged_list = []

    actual_merged_list = vals_to_list(
        solution.merge_two_lists(input_list_1, input_list_2)
    )
    assert actual_merged_list == expected_merged_list


def test_one_empty_list_and_one_non_empty_list_result_in_non_empty_list():
    solution = Solution()
    input_list_1 = None
    input_list_2 = ListNode(val=0, next=None)
    expected_merged_list = [0]

    actual_merged_list = vals_to_list(
        solution.merge_two_lists(input_list_1, input_list_2)
    )
    assert actual_merged_list == expected_merged_list
