class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        mp = Counter(nums)
        output = []
        for key in mp.most_common(k):
            output += [key[0]]
        return output
        
        
        
        
# ------------Another-Solution------------------------------        
        # frqL = {}
        # ans = []
        # for i in nums:
        #     frqL[i] = frqL.get(i,0) + 1
        # frqL = dict(sorted(frqL.items(),key=lambda item: item[1], reverse=True))
        # for key in list(frqL.keys())[:k]:
        #     ans.append(key)
        # return ans
