class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHq = []
        for num in nums:
            if len(minHq) == k:
                heappushpop(minHq, num)
            else:
                heappush(minHq, num)
        
        return minHq[0]