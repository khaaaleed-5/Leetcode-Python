class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return[0]
        mp = defaultdict(list)
        for i, j in edges:
            mp[i].append(j)
            mp[j].append(i)

        edge = {}
        leaf = deque()
        for x, y in mp.items():
            if len(y) == 1:
                leaf.append(x)
            edge[x] = len(y)

        while leaf:
            if n <= 2:
                return list(leaf)
            for i in range(len(leaf)):
                node = leaf.popleft()
                n -= 1
                for j in mp[node]:
                    edge[j] -= 1
                    if edge[j] == 1:
                        leaf.append(j)
