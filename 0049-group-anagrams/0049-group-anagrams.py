class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        cache = defaultdict(list)
        for i in range(len(strs)):
            val = "".join(sorted(strs[i]))
            cache[val].append(strs[i])

        res = []
        for i in cache.values():
            res.append(i)
        return res 