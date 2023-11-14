from grind75.week1.two_sum import find_two_indices_adding_up_to_target_sum


def test_two_numbers_at_indices_add_up_to_target_sum_case_1():
    input_numbers = [2, 7, 11, 15]
    input_target_sum = 9
    expected_numbers_indices = [0, 1]

    actual_numbers_indices = find_two_indices_adding_up_to_target_sum(
        input_numbers, input_target_sum
    )
    assert actual_numbers_indices == expected_numbers_indices


def test_two_numbers_at_indices_add_up_to_target_sum_case_2():
    input_numbers = [3, 2, 4]
    input_target_sum = 6
    expected_numbers_indices = [1, 2]

    actual_numbers_indices = find_two_indices_adding_up_to_target_sum(
        input_numbers, input_target_sum
    )
    assert actual_numbers_indices == expected_numbers_indices


def test_two_numbers_at_indices_add_up_to_target_sum_case_3():
    input_numbers = [3, 3]
    input_target_sum = 6
    expected_numbers_indices = [0, 1]

    actual_numbers_indices = find_two_indices_adding_up_to_target_sum(
        input_numbers, input_target_sum
    )
    assert actual_numbers_indices == expected_numbers_indices
