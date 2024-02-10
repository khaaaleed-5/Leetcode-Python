class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        l = 0
        r = n - 1
        while l < r:
            val = numbers[l] + numbers[r]
            if val == target:
                return [l + 1, r + 1]
            else:
                if val < target:
                    l += 1
                else:
                    r -= 1