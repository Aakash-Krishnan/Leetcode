class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
            # L = 0
            # R = len(word) -1 
            # flag = True
#             while L < R:
#                 if word[L] != word[R]:
#                     flag = False
#                     break
#                 L += 1
#                 R -= 1
#             if flag:
#                 return word
        
        return ""