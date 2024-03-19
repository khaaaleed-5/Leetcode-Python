from collections import Counter
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        mp = Counter(tasks)
        max_cnt = max(mp.values())
        max_task = 0
        for i in mp.values():
            if i == max_cnt:
                max_task += 1
        return max(((max_cnt - 1) * (n + 1) + max_task), len(tasks))
