class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        minHq = []
        n = len(nums)
        for _ in range(n):
            val = nums.pop()
            heappush(minHq, (val * val))
        for _ in range(n):
            nums.append(heappop(minHq))
        
        return nums