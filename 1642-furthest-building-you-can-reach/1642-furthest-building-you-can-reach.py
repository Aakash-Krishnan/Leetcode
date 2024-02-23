class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxHq = []
        for i in range(len(heights) - 1):
            if heights[i+1] <= heights[i]:
                continue
            diff = heights[i+1] - heights[i]
            bricks -= diff
            heappush(maxHq, -diff)
            if bricks < 0:
                if not ladders:
                    return i
                ladders -= 1
                bricks += -heappop(maxHq)
            
        return len(heights) - 1
        
        
        
        
        
        
        
        
        
#         for i in range(len(heights)-1):
#             if heights[i+1] <= heights[i]:
#                 continue
#             diff = heights[i+1] - heights[i]
            
#             bricks -= diff
#             heappush(maxHq, -diff)
#             if bricks < 0:
#                 if not ladders:
#                     return i
#                 ladders -= 1
#                 bricks += -heappop(maxHq)
        
#         return len(heights)-1
                    