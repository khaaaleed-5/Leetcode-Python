class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        #1 Brute Force method:
        # n = len(nums)
        # if nums.count(1) == nums.count(0):
        #     return n
        # ans = 0
        # for i in range(n):
        #     ones = 0
        #     zeros = 0
        #     l = 0
        #     for j in range(i, n):
        #         if nums[j] == 0:
        #             zeros += 1
        #         elif nums[j] == 1:
        #             ones += 1
        #         if zeros == ones:
        #             l = max(l, ones * 2)
        #     ans = max(ans, l)
        # return ans
        
        # -----------------------------------
        
        #2 prefix-sum and hashmap
        mp = {}
        s = 0
        ans = 0
        for i,val in enumerate(nums):
            s += 1 if val == 0 else -1
            if s == 0:
                ans = i + 1
            elif s in mp:
                ans = max(ans,i - mp[s])
            else:
                mp[s] = i
        return ans
