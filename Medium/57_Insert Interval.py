class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ans = []
        idx = 0
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            ans += [intervals[idx]]
            idx += 1
        while idx < len(intervals) and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[idx][0])
            newInterval[1] = max(newInterval[1], intervals[idx][1])
            idx += 1
        ans += [newInterval]
        while idx < len(intervals):
            ans += [intervals[idx]]
            idx += 1

        return ans