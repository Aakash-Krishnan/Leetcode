class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y','z'],
        }
        
        res = []
        
        def dfs(i, msg):
            if i == len(digits):
                if msg != "":
                    res.append(msg)
                return 
            
            for c in keypad[digits[i]]:
                dfs(i+1, msg + c)
                
        
        dfs(0, "")
        return res