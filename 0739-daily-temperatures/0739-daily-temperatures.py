class Solution:
    def dailyTemperatures(self, A: list[int]) -> list[int]:
        n = len(A)
        ans = [0] * n
        stack = []
        i, j = 0, 0
        
        while i < n:

            while stack and A[stack[-1]] < A[i]:
                idx = stack.pop()
                distance = i - idx
                ans[idx] = distance
                j += 1

            stack.append(i)
            i += 1
        return ans