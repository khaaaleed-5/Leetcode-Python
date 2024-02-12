from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        mp = Counter(nums)
        return mp.most_common(1)[0][0]

