class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while k and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            if stack or i != "0":
                stack.append(i)
        if k:
            stack = stack[ : -k]
        return "".join(stack) or "0"