class Solution:
    def numberOfMatches(self, n: int) -> int:
#         if n == 0:
#             return 0
        
#         if n != 1 and (n & 1):
#             val = self.numberOfMatches( ((n-1)//2) + 1)
#             return ((n-1)//2) + val
#         else:
#             val = self.numberOfMatches( n // 2 )
#             if (n//2) == 1:
#                 return (n//2)
#             return (n//2) + val
        return n-1