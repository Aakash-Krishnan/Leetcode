class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        maxHq = []
        
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                val = arr[i]/arr[j]
                if len(maxHq) < k:
                    heappush(maxHq, (-val, arr[i], arr[j]))
                elif -(maxHq[0][0]) > val:
                    heappop(maxHq)
                    heappush(maxHq, (-val, arr[i], arr[j]))
        return [maxHq[0][1], maxHq[0][2]]