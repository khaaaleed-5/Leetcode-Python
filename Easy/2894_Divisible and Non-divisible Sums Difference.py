class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        """
        s1: sum of numbers in [1, n] and not divisble by m
        s2: sum of numbers in [1, n] and divisble by m
        """
        s1 = ((n * n + n) // 2) - ((m * (n // m) * (1 + n // m)) // 2)
        s2 = (((n // m)) * (2 * m + (n // m - 1) * m) // 2)

        return s1 - s2
