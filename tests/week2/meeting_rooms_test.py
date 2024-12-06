from grind75.week2.meeting_rooms import Interval, Solution


def test_meeting_times_cannot_attend():
    intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    expected_result = False
    solution = Solution()

    actual_result = solution.can_attend_meetings(intervals)

    assert actual_result == expected_result


def test_meeting_times_can_attend():
    intervals = [Interval(5, 8), Interval(9, 15)]
    expected_result = True
    solution = Solution()

    actual_result = solution.can_attend_meetings(intervals)

    assert actual_result == expected_result


def test_meeting_end_equals_start_can_attend():
    intervals = [Interval(0, 8), Interval(8, 10)]
    expected_result = True
    solution = Solution()

    actual_result = solution.can_attend_meetings(intervals)

    assert actual_result == expected_result


def test_unsorted_meeting_end_equals_start_can_attend():
    intervals = [Interval(8, 10), Interval(0, 8)]
    expected_result = True
    solution = Solution()

    actual_result = solution.can_attend_meetings(intervals)

    assert actual_result == expected_result


def test_unsorted_can_attend():
    intervals = [Interval(9, 15), Interval(5, 8)]
    expected_result = True
    solution = Solution()

    actual_result = solution.can_attend_meetings(intervals)

    assert actual_result == expected_result
