from collections import Counter
class Solution:
    def isPossibleToSplit(self, nums: list[int]) -> bool:
        if len(nums) % 2:
            return False
        mp = Counter(nums)
        if mp.most_common(1)[0][1] > 2:
            return False
        return True