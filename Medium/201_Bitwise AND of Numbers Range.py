class Solution:
    def singleNumber(self, a: int, b: int) -> int:
        result = 0
        while a < b:
            a >>= 1
            b >>= 1
            result += 1
        return a << result