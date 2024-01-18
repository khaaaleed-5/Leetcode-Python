class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = sorted(set(nums))
        cnt = 1
        ans = [1]
        for i in range(len(nums) - 1):
            if (nums[i] + 1 == nums[i + 1]):
                cnt += 1
            else:
                ans.append(cnt)
                cnt = 1
            ans.append(cnt)
        if not nums:
            return 0
        else:
            return max(ans)