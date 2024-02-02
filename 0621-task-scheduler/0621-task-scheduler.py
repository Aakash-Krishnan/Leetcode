class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHq = [-i for i in counter.values()]
        heapify(maxHq)
        q = deque()
        time = 0
        
        while q or maxHq:
            time += 1
            if maxHq:
                cnt = 1 + heappop(maxHq)
                if cnt:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heappush(maxHq, q.popleft()[0])
        
        return time
                    