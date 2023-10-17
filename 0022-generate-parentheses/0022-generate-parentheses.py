import sys
class Solution:
    sys.setrecursionlimit(10**5)
    def generateParenthesis(self, n: int) -> List[str]:

        def param(A, n, op, cl):
            arr = []
            if len(A) == 2*n:
                arr.append(A)
                return arr
            
            if op < n:
                arr += param(A+"(", n, op+1, cl)
            if op > cl:
                arr += param(A+")", n, op, cl+1)
            return arr
        
        return param("", n, 0, 0)