class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        mp = defaultdict(list)
        for i in range(len(nums)):
            for j in mp[nums[i]]:
                if (i * j) % k == 0:
                    ans += 1
            mp[nums[i]] += [i]
        return ans
