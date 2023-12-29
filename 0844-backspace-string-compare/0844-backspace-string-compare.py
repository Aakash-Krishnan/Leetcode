class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        Sstack = []
        Tstack = []
        
        for i in s:
            if i == "#":
                if Sstack:
                    Sstack.pop()
            else:
                Sstack.append(i)
        
        for i in t:
            if i == "#":
                if Tstack:
                    Tstack.pop()
            else:
                Tstack.append(i)
        
        return True if Sstack == Tstack else False