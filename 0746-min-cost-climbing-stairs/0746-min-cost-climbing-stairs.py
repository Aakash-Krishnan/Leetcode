class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])
        
#         cache = [-1 for i in range(len(cost)+1)]
#         def dfs(i, Sum=0):
#             if i >= len(cost):
#                 return 0
#             if cache[i] != -1:
#                 return cache[i]
            
#             res = min(dfs(i+1, Sum), dfs(i+2, Sum)) + cost[i]
#             cache[i] = res
#             return res
        
#         return min(dfs(0), dfs(1))