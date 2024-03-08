class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxHq = []
        for key, freq in count.items():
            heappush(maxHq, -freq)
            
        res = -maxHq[0]
        prev = heappop(maxHq)
        
        while maxHq and maxHq[0] == prev:
            res -= heappop(maxHq)
        
        return res