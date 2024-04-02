class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        mp2 = {}
        n = len(s)
        for i in range(n):
            if s[i] not in mp and t[i] not in mp2:
                mp[s[i]] = t[i]
                mp2[t[i]] = s[i]
            else:
                if s[i] not in mp or t[i] not in mp2:
                    return False
                if mp[s[i]] != t[i] or mp2[t[i]] != s[i]:
                    return False
        return True
