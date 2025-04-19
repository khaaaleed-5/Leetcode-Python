class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] <= upper:
                  ans += (r - l)
                  l += 1
            else:
                  r -= 1
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] < lower:
                ans -= (r - l)
                l += 1
            else:
                r -= 1

        return ans
