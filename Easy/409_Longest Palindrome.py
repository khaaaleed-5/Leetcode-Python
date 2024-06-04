class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = Counter(s)
        ans = 0
        for val in mp.values():
            if ans & 1 and val & 1:
                val -= 1
                ans += val
            else:
                ans += val
        return ans
