class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        if digits.count(9) == n:
            return [1] + [0] * n
        i = n - 1
        if digits[i] != 9:
            digits[i] += 1
            return digits
        else:
            for j in range(i, -1, -1):
                if digits[j] == 9:
                    digits[j] = 0
                else:
                    i = j
                    break
            digits[i] += 1
        return digits
