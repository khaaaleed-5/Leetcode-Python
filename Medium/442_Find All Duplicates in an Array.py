from collections import Counter
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        mp = Counter(nums)
        l = [i for i, j in mp.items() if j == 2]
        return l