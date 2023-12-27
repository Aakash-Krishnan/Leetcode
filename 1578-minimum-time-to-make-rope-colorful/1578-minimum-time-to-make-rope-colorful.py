class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        front, back = 1, 0
        ans = 0
        
        while front < len(colors):
            if colors[front] == colors[back]:
                if neededTime[front] < neededTime[back]:
                    ans += neededTime[front]
                    # front+= 1
                else:
                    ans += neededTime[back]
                    back = front
                    # front += 1
            else:
                back = front
            front += 1
        return ans