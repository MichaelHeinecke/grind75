# https://leetcode.com/problems/two-sum/description/
from typing import List, Dict


def find_two_indices_adding_up_to_target_sum(
    numbers: List[int], target_sum: int
) -> List[int]:
    """Finds the indexes of two numbers in the given list that add up to the given
    target sum.

    Each input is expected to have exactly one solution, and each number in the input
    list can only occur once.

    :param numbers: List of numbers to search through.
    :param target_sum: The target sum to which two numbers in the `numbers` list should
    add up to.
    :return: List of the two indexes pertaining to the two numbers in the given list
    that add up to the given target sum.
    """
    # The idea is to keep track of the differences between the target sum and the
    # numbers in the list, and their indexes. If the difference between the target sum
    # and a number in the list is already in the dictionary, then we have found the
    # two numbers that add up to the target sum.
    # Solution has time complexity O(n) and space complexity O(n).
    seen_diffs_indexes_dict: Dict[int, int] = {}

    for i, number in enumerate(numbers):
        diff = target_sum - number
        if diff in seen_diffs_indexes_dict:
            return [seen_diffs_indexes_dict[diff], i]
        else:
            seen_diffs_indexes_dict[number] = i
