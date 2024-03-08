class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        Max = max(count.values())
        res = 0
        for key, freq in count.items():
            if freq == Max:
                res += 1
        
        return res * Max