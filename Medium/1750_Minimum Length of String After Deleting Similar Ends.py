class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        l = 0
        r = n - 1
        while l < r:
            c = s[l]
            if s[l] != s[r]:
                break
            else:
                l += 1
                r -= 1
                n -= 2
                while l <= r:
                    if s[l] == c:
                        n -= 1
                        l += 1
                    if s[l] != c:
                        break
                while l <= r:
                    if s[r] == c:
                        n -= 1
                        r -= 1
                    if s[r] != c:
                        break
        return n