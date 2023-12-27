class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        pt1, pt2 = 1, 0
        ans = 0
        
        while pt1 < len(colors):
            if colors[pt1] == colors[pt2]:
                if neededTime[pt1] < neededTime[pt2]:
                    ans += neededTime[pt1]
                    pt1+= 1
                else:
                    ans += neededTime[pt2]
                    pt2 = pt1
                    pt1 += 1
            else:
                pt2 = pt1
                pt1 += 1
        return ans