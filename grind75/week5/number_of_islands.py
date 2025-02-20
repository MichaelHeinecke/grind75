from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def bfs(row, col):
            queue: (int, int) = deque([(row, col)])
            visited.add((row, col))

            while queue:
                row, col = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    r, c = row + dr, col + dc
                    if (
                        0 <= r < rows
                        and 0 <= c < cols
                        and grid[r][c] == "1"
                        and (r, c) not in visited
                    ):
                        queue.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    num_islands += 1

        return num_islands
