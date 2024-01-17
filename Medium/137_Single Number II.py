class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dec = {}
        for i in nums:
            dec[i] = dec.get(i, 0) + 1
        for i, j in dec.items():
            if j == 1:
                return i