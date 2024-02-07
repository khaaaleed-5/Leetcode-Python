class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s2 = s.split(' ')
        if len(s2) != len(pattern):
            return False
        mp = {}
        occ = []
        for i in range(len(pattern)):
            if pattern[i] not in mp:
                if s2[i] not in occ:
                    mp[pattern[i]] = mp.get(pattern[i],'') + s2[i]
                    occ.append(s2[i])
                else:
                    return False
            else:
                if mp[pattern[i]] != s2[i]:
                    return False
        return True