class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        mid = (l + r) // 2
        while l <= r:
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            mid = (l + r) // 2
        return -1
