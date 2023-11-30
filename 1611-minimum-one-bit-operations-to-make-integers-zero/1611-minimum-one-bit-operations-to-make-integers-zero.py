class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        arr = [1] * 31
        for i in range(1, len(arr)):
            arr[i] = (2 * arr[i-1]) + 1
        ans = 0
        plus = 1

        for i in range(30, -1, -1):
            isOne = n&(1<<i) > 0
            if not isOne: continue

            if plus: ans += arr[i]
            else: ans -= arr[i]
            plus ^= 1
        return ans