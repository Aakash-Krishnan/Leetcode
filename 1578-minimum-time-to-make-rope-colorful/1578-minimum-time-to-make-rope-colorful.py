class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = (colors[0], 0)
        res = 0
        
        for i in range(1, len(neededTime)):
            if colors[i] == prev[0]:
                if neededTime[i] < neededTime[prev[1]]:
                    res += neededTime[i]
                else:
                    res += neededTime[prev[1]]
                    prev = [colors[i], i]
            else:
                prev = [colors[i], i]
        return res