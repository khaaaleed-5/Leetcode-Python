class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        ans = [[], []]
        match = {}
        for i in matches:
            match[i[0]] = match.get(i[0], 0) + 0
            match[i[1]] = match.get(i[1], 0) + 1
        for i, j in match.items():
            if j == 0:
                ans[0].append(i)
            elif j == 1:
                ans[1].append(i)

        ans[0] = sorted(ans[0])
        ans[1] = sorted(ans[1])
        return ans
