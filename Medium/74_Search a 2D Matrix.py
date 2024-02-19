class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix)
        for i in range(n):
            m = len(matrix[i]) - 1
            if matrix[i][m] < target:
                continue
            else:
                l, r = 0, m
                while l <= r:
                    m = (l + r) // 2
                    if matrix[i][m] == target:
                        return True
                    if matrix[i][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
        return False