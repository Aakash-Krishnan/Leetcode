class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHq = []
        
        for x, y in points:
            dist = -(x*x + y*y)
            if len(minHq) == k:
                heappushpop(minHq, (dist, x, y))
            else:
                heappush(minHq, (dist, x, y))
        
        return [(x, y) for dist, x, y in minHq]