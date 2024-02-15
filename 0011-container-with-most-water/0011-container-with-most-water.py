class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        lmax, rmax = 0, len(height)-1
        while lmax < rmax:
            h = min(height[lmax], height[rmax])
            w = rmax - lmax
            res = max(res, w * h)
            if height[lmax] < height[rmax]:
                lmax += 1
            else:
                rmax -= 1
        
        return res
        