class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        s = ''
        ss = ''
        for i in word1:
            s += i
        for i in word2:
            ss += i
        if s == ss:
            return True
        return False