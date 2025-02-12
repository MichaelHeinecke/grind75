import pytest

from grind75.week5.course_schedule import Solution


@pytest.mark.parametrize(
    "num_courses, prerequisites, expected_result",
    [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (4, [[1, 0], [2, 1], [3, 2], [4, 2]], True),
        (5, [[1, 0], [2, 1], [3, 2], [4, 2], [5, 3]], True),
        (5, [[1, 0], [2, 1], [3, 2], [4, 2], [5, 3], [5, 4]], True),
        (4, [[1, 2], [3, 4]], True),
        (3, [[1, 0], [2, 1], [0, 2]], False),
    ],
)
def test_course_schedule_is_possible(
    num_courses: int, prerequisites: list[list[int]], expected_result: bool
):
    actual_result = Solution().canFinish(num_courses, prerequisites)
    assert actual_result == expected_result
