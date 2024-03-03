class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        wordList.append(beginWord)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                graph[pattern].append(word)
        
        q = deque([(beginWord, 1)])
        visit = set([beginWord])
        
        while q:
            word, res = q.popleft()
            if word == endWord:
                return res
            for j in range(len(word)):
                pattern = word[:j] +'*'+ word[j+1:]
                for nei in graph[pattern]:
                    if nei not in visit:
                        q.append((nei, res + 1))
                        visit.add(nei)
        return 0