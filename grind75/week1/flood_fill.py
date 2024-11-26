# You are given an image represented by an m x n grid of integers image, where
# image[i][j] represents the pixel value of the image. You are also given three
# integers sr, sc, and color. Your task is to perform a flood fill on the image
# starting from the pixel image[sr][sc].
#
# To perform a flood fill:
#
# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that
# share a side with the original pixel, either horizontally or vertically) and
# shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated
# pixels and modifying their color if it matches the original color of the
# starting pixel. The process stops when there are no more adjacent pixels of
# the original color to update.
# Return the modified image after performing the flood fill.
class Solution:
    def floodFill(
        self, image: list[list[int]], row: int, col: int, color: int
    ) -> list[list[int]]:
        def flood_fill_recurse(
            image: list[list[int]], row: int, col: int, color: int, base_color: int
        ):
            if image[row][col] == color:
                return

            image[row][col] = color

            if col - 1 >= 0 and image[row][col - 1] == base_color:  ## recurse left
                flood_fill_recurse(image, row, col - 1, color, base_color)

            if (
                col + 1 < len(image[row]) and image[row][col + 1] == base_color
            ):  ## recurse right
                flood_fill_recurse(image, row, col + 1, color, base_color)

            if row - 1 >= 0 and image[row - 1][col] == base_color:  ## recurse up
                flood_fill_recurse(image, row - 1, col, color, base_color)

            if (
                row + 1 < len(image) and image[row + 1][col] == base_color
            ):  ## recurse down
                flood_fill_recurse(image, row + 1, col, color, base_color)

        base_color = image[row][col]
        flood_fill_recurse(image, row, col, color, base_color)
        return image
