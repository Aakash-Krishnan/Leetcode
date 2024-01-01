class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        mod = (10**9) + 7

        def nearestSmallest(right=False):
            NS = [-1] * n
            stack = []
            if not right:
                for i in range(n):
                    while stack and arr[stack[-1]] >= arr[i]:
                        stack.pop()    
                    if stack:
                        NS[i] = stack[-1]
                    stack.append(i)            
            else:
                for i in range(n-1, -1, -1):
                    while stack and arr[stack[-1]] > arr[i]:
                        stack.pop()                        
                    if stack:
                        NS[i] = stack[-1]
                    else:
                        NS[i] = n
                    stack.append(i)
            return NS
        
        min_sum = 0
        NSL = nearestSmallest()
        NSR = nearestSmallest(True)
        for i in range(n):
            min_sum = ( min_sum + (arr[i] * ((i - NSL[i]) * (NSR[i] - i)))) % mod
        return min_sum