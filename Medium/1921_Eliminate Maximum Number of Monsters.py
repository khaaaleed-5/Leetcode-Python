import math
class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        minutes = []
        for i in range(len(speed)):
            minutes += [math.ceil(dist[i] / speed[i])]
        cnt = 0
        sec = 0
        minutes.sort()
        for i in minutes:
            if i <= sec:
                return cnt
            cnt += 1
            sec += 1
        return cnt