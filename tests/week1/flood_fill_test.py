from grind75.week1.flood_fill import Solution


def test_adjacent_pixels_are_flipped():
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr, sc, color = 1, 1, 2
    expected_image = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

    solution = Solution()
    assert solution.floodFill(image, sr, sc, color) == expected_image


def test_nothing_to_flip():
    image = [[0, 0, 0], [0, 0, 0]]
    sr, sc, color = 0, 0, 0
    expected_image = [[0, 0, 0], [0, 0, 0]]

    solution = Solution()
    assert solution.floodFill(image, sr, sc, color) == expected_image
