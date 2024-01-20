class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        mod = 10e9 + 7
        result = 0
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                j = stack.pop()
                result += arr[j] * (i - j) * (j - stack[-1] if stack else j + 1)
            stack.append(i)

        while stack:
            j = stack.pop()
            result += arr[j] * (n - j) * (j - stack[-1] if stack else j + 1)

        return int(result % mod)