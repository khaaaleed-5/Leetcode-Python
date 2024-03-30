class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mp = {}
        max_sub = -1
        for i in range(len(s)):
            if s[i] in mp:
                max_sub = max(max_sub,i - mp[s[i]])
            else:
                mp[s[i]] = i + 1
        return max_sub
