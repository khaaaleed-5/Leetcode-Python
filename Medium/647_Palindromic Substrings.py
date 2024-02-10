class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = n
        for i in range(n):
            ss = s[i]
            for j in range(i + 1, n):
                ss += s[j]
                test = ss[::-1]
                if test == ss:
                    cnt += 1
        return cnt