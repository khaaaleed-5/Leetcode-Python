class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        def min_cost(matrix, i, j, cnt_s, memo):
            if i == len(matrix) - 1:
                return matrix[i][j]

            if (i, j) in memo:
                return memo[(i, j)]

            if j == 0:
                result = matrix[i][j] + min(min_cost(matrix, i + 1, j, cnt_s, memo),
                                            min_cost(matrix, i + 1, j + 1, cnt_s, memo))
            elif j == len(matrix[0]) - 1:
                result = matrix[i][j] + min(min_cost(matrix, i + 1, j, cnt_s, memo),
                                            min_cost(matrix, i + 1, j - 1, cnt_s, memo))
            else:
                result = matrix[i][j] + min(min_cost(matrix, i + 1, j - 1, cnt_s, memo),
                                            min_cost(matrix, i + 1, j, cnt_s, memo),
                                            min_cost(matrix, i + 1, j + 1, cnt_s, memo))

            memo[(i, j)] = result
            return result

        cnt_s = [0] * len(matrix[0])
        memo = {}

        for j in range(len(matrix[0])):
            cnt_s[j] = min_cost(matrix, 0, j, cnt_s, memo)
        return min(cnt_s)