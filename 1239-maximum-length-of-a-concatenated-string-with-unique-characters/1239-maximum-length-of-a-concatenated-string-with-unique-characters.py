class Solution:
    def maxLength(self, arr: list[str]) -> int: 

        def isEqual(word1, word2):
            wordset = set(word1)
            for i in word2:
                if i in wordset:
                    return True
            return False 
            
        # res = 0
        def check(idx, word=""):
            # nonlocal res
            if idx == len(arr):
                # res = max(res, len(word))
                return len(word)
            
            if len(set(arr[idx])) != len(arr[idx]):
                return check(idx + 1, word)
            res = 0
            if not isEqual(word, arr[idx]):
                res = check(idx + 1, word + arr[idx])

            return max(res, check(idx+1, word))
        # check(0)
        return check(0)