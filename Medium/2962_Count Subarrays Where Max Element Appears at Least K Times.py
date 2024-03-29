class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        n = len(nums)
        l, r, ans = 0, 0, 0
        max_elm = max(nums)
        cnt, ans = 0, 0

        while r < n:
            k -= nums[r] == max_elm
            while k == 0:
                k += nums[l] == max_elm
                l += 1
            ans += l
            r += 1

        return ans
