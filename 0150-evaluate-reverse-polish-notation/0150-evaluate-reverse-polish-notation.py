class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        def popOut():
            val2 = stack.pop()
            val1 = stack.pop()
            return val1, val2
        
        for i in tokens:
            val1, val2 = popOut() if i in ["+", "-", "*", "/"] else (0, 0)
            match i:
                case "+":
                    stack.append(val1 + val2)
                    continue
                case "-":
                    stack.append(val1 - val2)
                    continue
                case "*":
                    stack.append(val1 * val2)
                    continue
                case "/":
                    stack.append(int(val1 / val2))
                    continue
                case default:
                    stack.append(int(i))
        
        return stack[-1]