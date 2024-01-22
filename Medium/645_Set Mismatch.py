class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        mp = [0] * n
        for i in nums:
            mp[i - 1] += 1
        elm1 = mp.index(max(mp))
        elm2 = mp.index(min(mp))
        return [elm1 + 1, elm2 + 1]