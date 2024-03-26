from collections import Counter
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        mp = Counter(nums)
        cnt = 1
        for i in range(len(mp)):
            if cnt not in mp:
                return cnt
            cnt += 1
        return cnt