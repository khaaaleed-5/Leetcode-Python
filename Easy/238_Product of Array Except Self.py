class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        value = 1
        ans = []
        cnt_0 = nums.count(0)
        if cnt_0 > 1:
            return [0] * len(nums)
        for i in nums:
            if i != 0:
                value *= i
        for i in nums:
            if cnt_0:
                if i == 0:
                    ans.append(value)
                else:
                    ans.append(0)
            else:
                ans.append(int(value / i))
        return ans