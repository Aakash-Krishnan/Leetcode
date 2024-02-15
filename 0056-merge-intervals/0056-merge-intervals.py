class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if not(res[-1][1] < intervals[i][0] or intervals[i][1] < res[-1][0]):
                res[-1] = [min(res[-1][0], intervals[i][0]), max(res[-1][1], intervals[i][1])]
            else:
                res.append(intervals[i])
            
        return res