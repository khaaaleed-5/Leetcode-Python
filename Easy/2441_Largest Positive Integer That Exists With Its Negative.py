class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        mp = Counter(nums)
        mx = -1
        for i in mp.keys():
            if -i in mp:
                mx = max(i, mx)
        return mx
