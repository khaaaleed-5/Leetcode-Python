class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 1
        l, r = 0, 0
        mp = {}
        while r < n:
            mp[nums[r]] = mp.get(nums[r], 0) + 1
            while mp[nums[r]] > k:
                mp[nums[l]] -= 1
                l += 1
            ans = max(ans,sum(mp.values()))
            r += 1
        return ans
