from collections import Counter
import math
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        mp = Counter(nums)
        op = 0
        cnt = 0
        for i, j in mp.items():
            if j == 1:
                return -1
            op += math.ceil(j / 3)
            cnt += j
        if cnt == len(nums):
            return op
        return -1