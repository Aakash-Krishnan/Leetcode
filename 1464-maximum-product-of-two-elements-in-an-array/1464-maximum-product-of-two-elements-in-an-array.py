class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        hq = []
        for i in nums:
            if len(hq) < 2:
                heappush(hq, i)
            elif hq[0] < i:
                heappop(hq)
                heappush(hq, i) 
            
        return (hq[0] - 1) * (hq[1] - 1)