class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        def isPrefixAndSuffix(str1: str, str2: str):
            if str1 == str2[:len(str1)] and str1 == str2[-len(str1):]:
                return True
            return False

        n = len(words)
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    cnt += 1
        return cnt
    
"""
    another solution :
    
        n = len(words)
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    cnt += 1
        return cnt
        
"""