class Solution:
    def countAndSay(self, n: int) -> str:
        def sequence(s: str) -> str:
            ans = ''
            i = 0
            while i < len(s):
                count = 1
                while i < len(s) - 1 and s[i] == s[i + 1]:
                    count += 1
                    i += 1
                ans = ans + str(count) + s[i]
                i += 1
            return ans

        current = '1'
        for i in range(1, n):
            current = sequence(current)
        return current
