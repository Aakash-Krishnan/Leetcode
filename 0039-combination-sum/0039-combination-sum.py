class Solution:
    def combinationSum(self, A: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, Sum, arr):
            if i == len(A) or Sum > target:
                return 0
            if target == Sum:
                res.append(arr.copy())
                return 
            
            dfs(i + 1, Sum, arr)
            arr.append(A[i])
            dfs(i, Sum + A[i], arr)
            arr.pop()
            return 0
        
        dfs(0, 0, [])
        return res