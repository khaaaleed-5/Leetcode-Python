class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ans = 1001
        while l <= r:
            mid = (l + r) // 2
            ans = min(ans,nums[mid])
            if min(nums[mid],min(nums[l],nums[r])) == nums[mid] or nums[l] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        return ans
