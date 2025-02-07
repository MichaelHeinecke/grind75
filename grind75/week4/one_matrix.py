from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height = len(mat)
        width = len(mat[0])
        queue: List[(int, int)] = []

        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1  # mark non-zero cells as not visited

        for row, column in queue:
            for diff_row, diff_column in (0, -1), (0, 1), (-1, 0), (1, 0):
                next_row = row + diff_row
                next_column = column + diff_column

                if (
                    0 <= next_row < height
                    and 0 <= next_column < width
                    and mat[next_row][next_column] == -1
                ):
                    mat[next_row][next_column] = mat[row][column] + 1
                    queue.append((next_row, next_column))

        return mat
