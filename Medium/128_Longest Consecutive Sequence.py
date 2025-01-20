class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        ans = 0
        for num in nums:
            if num - 1 not in nums:
                idx = 1
                while num + idx in nums:
                    idx += 1
                ans = max(ans,idx)
        return ans


# -----------------Another-Solution----------------------- O(nlogn)       
#         nums = sorted(set(nums))
#         cnt = 1
#         ans = [1]
#         for i in range(len(nums) - 1):
#             if (nums[i] + 1 == nums[i + 1]):
#                 cnt += 1
#             else:
#                 ans.append(cnt)
#                 cnt = 1
#             ans.append(cnt)
#         if not nums:
#             return 0
#         else:
#             return max(ans)
