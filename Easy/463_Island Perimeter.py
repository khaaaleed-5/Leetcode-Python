class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        s = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if j == 0 or grid[i][j - 1] == 0:
                        s += 1
                    if j == m - 1 or grid[i][j + 1] == 0:
                        s += 1
                    if i == 0 or grid[i - 1][j] == 0:
                        s += 1
                    if i == n - 1 or grid[i + 1][j] == 0:
                        s += 1
        return s
