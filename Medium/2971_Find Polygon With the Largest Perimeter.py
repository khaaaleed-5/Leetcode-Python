class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
        max_per = 0
        for i in range(2, n):
            if prefix[i - 1] > nums[i]:
                if prefix[i] > max_per:
                    max_per = prefix[i]
        return max_per if max_per > 0 else -1