import pytest

from grind75.week4.reverse_bits import Solution


@pytest.mark.parametrize(
    "n, expected_result",
    [
        (0b00000010100101000001111010011100, 964176192),
        (0b11111111111111111111111111111101, 3221225471),
    ],
)
def test_bits_are_reversed(n, expected_result):
    actual_result = Solution().reverseBits(n)
    assert actual_result == expected_result
