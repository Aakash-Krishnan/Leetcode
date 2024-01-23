class Solution:
    def maxLength(self, arr: list[str]) -> int: 
        cache = []
        for i in arr:
            sub = set(i)
            if len(i) == len(sub):
                cache.append(sub)
            else:
                cache.append(-1)
                

        def isEqual(word1, word2):

            for i in word1:
                if i in word2:
                    return True
            return False 
            
        def check(idx, word=""):
            if idx == len(arr):
                return len(word)
            
            # If the string itself has duplicate chars we can skip 
            if cache[idx] == -1:
                return check(idx + 1, word)
            
            res = 0
            if not isEqual(word, cache[idx]):
                res = check(idx + 1, word + arr[idx])

            return max(res, check(idx+1, word))
        return check(0)