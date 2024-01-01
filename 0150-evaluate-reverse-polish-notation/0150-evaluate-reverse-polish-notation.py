class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        def popOut():
            val2 = stack.pop()
            val1 = stack.pop()
            return val1, val2
        
        for i in tokens:
            match i:
                case "+":
                    val1, val2 = popOut()
                    stack.append(val1 + val2)
                case "-":
                    val1, val2 = popOut()
                    stack.append(val1 - val2)
                case "*":
                    val1, val2 = popOut()
                    stack.append(val1 * val2)
                case "/":
                    val1, val2 = popOut()
                    stack.append(int(val1 / val2))
                case default:
                    stack.append(int(i))
        
        return stack[-1]