class Solution:
    def badPair(self, a: str, b: str) -> bool:
        if a.lower() == b.lower():
            if (a.isupper() and b.islower()) or (a.islower() and b.isupper()):
                return True
        return False
    def makeGood(self, s: str) -> str:
        n = len(s)
        st = [s[0]]
        for i in range(1, n):
            if st and self.badPair(st[-1],s[i]):
                st.pop()
            else:
                st += [s[i]]
        return ''.join(i for i in st)