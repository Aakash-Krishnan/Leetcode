class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                sub = ''
                while stack[-1] != '[':
                    sub = stack.pop() + sub
                stack.pop()
                
                n = ''
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n
                
                stack.append(int(n) * sub)
        
        return "".join(stack)