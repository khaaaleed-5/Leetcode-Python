class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = score.copy()
        ans = []
        mp = {}
        arr.sort(reverse=True)
      
        for i,j in enumerate(arr):
            mp[j] = i
          
        for i in score:
            if mp[i] < 3:
                if mp[i] == 0:
                    ans += ["Gold Medal"]
                elif mp[i] == 1:
                    ans += ["Silver Medal"]
                else:
                    ans += ["Bronze Medal"]
            else:
                ans += [f"{mp[i] + 1}"]
              
        return ans
