class Solution:
    def combinationSum(self, A: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, Sum, arr):
            nonlocal res
            if i == len(A) or Sum > target:
                return 0
            if Sum == target:
                res.append(arr.copy())
                return 0

            arr.append(A[i])
            dfs(i, Sum + A[i], arr)
            arr.pop()
            dfs(i+1, Sum, arr)
            
            return 0
        dfs(0, 0, [])
        return res