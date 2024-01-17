class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cache  = Counter(arr)
        dup = set()
        for i in cache.values():
            if i in dup:
                return False
            dup.add(i)
        
        return True