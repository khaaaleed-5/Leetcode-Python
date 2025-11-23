class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        flag = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                ans += 1
                flag += 1
                if flag > 1:
                    ans += flag - 1
            else:
                flag = 0
        return ans
