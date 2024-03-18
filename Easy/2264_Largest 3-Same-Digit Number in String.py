class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = -1
        for i in range(2, len(num)):
            if num[i] == num[i - 1] == num[i - 2]:
                ans = max(ans, int(num[i]))
        return "" if ans == -1 else str(ans) * 3