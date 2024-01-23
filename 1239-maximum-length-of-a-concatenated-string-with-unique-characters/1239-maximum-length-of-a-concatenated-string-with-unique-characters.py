class Solution:
    def maxLength(self, arr: list[str]) -> int: 
        res = 0

        def isEqual(word1, word2):
            wordset = set(word1)
            for i in word2:
                if i in wordset:
                    return True
            return False 
            

        def check(idx, word=""):
            nonlocal res
            if idx == len(arr):
                res = max(res, len(word))
                return 
            
            if len(set(arr[idx])) != len(arr[idx]):
                return check(idx + 1, word)
            
            if not isEqual(word, arr[idx]):
                check(idx + 1, word + arr[idx])

            check(idx+1, word)
        check(0)
        return res