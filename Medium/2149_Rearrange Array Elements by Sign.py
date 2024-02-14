class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        a, b = 0, 1
        for i in nums:
            if i > 0:
                ans[a] = i
                a += 2
            else:
                ans[b] = i
                b += 2
        return ans