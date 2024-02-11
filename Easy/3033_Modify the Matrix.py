class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        max_values = [max(column) for column in zip(*matrix)]
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == -1:
                    matrix[i][j] = max_values[j]
        return matrix