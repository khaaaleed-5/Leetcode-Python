class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        if len(set(nums)) == len(nums):
            return len(nums)
        frq = Counter(nums)
        frq = dict(sorted(frq.items(), key=lambda item: item[1], reverse=True))
        value = list(frq.values())[0]
        cnt = 0
        for i in frq.values():
            if i == value:
                cnt += i
            else:
                break
        return cnt