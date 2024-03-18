class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        arrow = -2e10
        cnt = 0
        for i in points:
            if i[1] >= arrow >= i[0]:
                continue
            else:
                cnt += 1
                arrow = i[1]
        return cnt