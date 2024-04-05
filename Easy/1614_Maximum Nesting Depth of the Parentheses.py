class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        cnt = 0
        for i in s:
            if i == '(':
                cnt += 1
            elif i == ')':
                cnt -= 1
            ans = max(ans,cnt)
        return ans
