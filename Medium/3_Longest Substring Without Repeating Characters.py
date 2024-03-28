class Solution:
    def maxSubarrayLength(self, s: str) -> int:
        n = len(s)
        ans = 1
        l, r = 0, 0
        mp = {}
        while r < n:
            mp[s[r]] = mp.get(s[r], 0) + 1
            while mp[s[r]] > 1:
                mp[s[l]] -= 1
                l += 1
            ans = max(ans,r - l + 1)
            r += 1
        return ans
