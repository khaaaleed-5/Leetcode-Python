class Solution:
    def countLargestGroup(self, n: int) -> int:
      mp = {}
      for i in range(1, n + 1):
            val = i
            s = 0
            while val > 0:
                  s += (val % 10)
                  val //= 10
            mp[s] = mp.get(s, 0) + 1
      max_size = max(mp.values())
      ans = sum(1 for x in mp.values() if x == max_size)
      return ans
