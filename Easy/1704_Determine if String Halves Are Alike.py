class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        if n % 2:
            return False
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        cnt_1 = 0
        cnt_2 = 0
        for i in range(n):
            if s[i] in vowels and i < n / 2:
                cnt_1 += 1
            elif s[i] in vowels and i >= n / 2:
                cnt_2 += 1
        return cnt_2 == cnt_1